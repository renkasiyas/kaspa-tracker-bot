# ABOUTME: Callback query handlers for interactive bot UI
# ABOUTME: Handles all button clicks and interactive elements

import asyncio
import logging
from typing import Any, Dict, Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler

from ..clients.kaspa_api import KaspaAPI
from ..clients.kaspa_grpc import KaspaGrpcClient
from ..db.database import Database
from .bot_ui import BotUI

logger = logging.getLogger(__name__)

# Conversation states
WAITING_ADDRESS, WAITING_LABEL = range(2)


class CallbackHandlers:
    """Handles all callback queries from inline keyboards"""

    def __init__(self, db: Database, kaspa_api: KaspaAPI, kaspa_client: KaspaGrpcClient):
        self.db = db
        self.kaspa_api = kaspa_api
        self.kaspa_client = kaspa_client
        self.ui = BotUI()

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Main callback query handler"""
        query = update.callback_query
        await query.answer()

        data = query.data
        user_id = query.from_user.id

        # Delete all messages after this one to clean up the chat
        try:
            current_msg_id = query.message.message_id
            chat_id = query.message.chat_id

            # Store the last message ID we know about to avoid unnecessary deletion attempts
            last_msg_id = context.user_data.get("last_bot_msg_id", current_msg_id + 10)

            # Try to delete messages after this one (up to the last known message)
            for i in range(1, min(last_msg_id - current_msg_id + 1, 20)):
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=current_msg_id + i)
                    await asyncio.sleep(0.05)  # Small delay to avoid rate limiting
                except Exception:
                    # Message doesn't exist or can't be deleted, silently continue
                    break  # If one fails, likely the rest don't exist either
        except Exception:
            # Silently ignore any deletion errors
            pass

        # Main menu handlers
        if data == "menu_main":
            await self.show_main_menu(query)
        elif data == "menu_add":
            await self.start_add_address(query, context)
        elif data == "menu_list":
            await self.show_address_list(query, user_id)

        # Address view handlers
        elif data.startswith("addr_v_"):
            index = int(data.replace("addr_v_", ""))
            addresses = await self.db.get_user_addresses(user_id)
            if index < len(addresses):
                address = addresses[index]["address"]
                await self.show_address_detail(query, user_id, address, context)
        elif data.startswith("addr_bal_"):
            # Store address in user_data and retrieve it
            address = context.user_data.get("current_address")
            if address:
                await self.check_balance(query, address)
        elif data.startswith("addr_utxo_"):
            address = context.user_data.get("current_address")
            if address:
                await self.show_utxos(query, address)
        elif data.startswith("addr_tx_"):
            address = context.user_data.get("current_address")
            if address:
                await self.show_transactions(query, address)
        elif data.startswith("addr_lbl_"):
            address = context.user_data.get("current_address")
            if address:
                await self.start_edit_label(query, context, address)
        elif data.startswith("addr_rm_"):
            address = context.user_data.get("current_address")
            if address:
                await self.confirm_remove(query, context, address)
        elif data == "confirm_rm":
            address = context.user_data.get("current_address")
            if address:
                await self.remove_address(query, user_id, address)

        # List pagination
        elif data.startswith("list_page_"):
            page = int(data.replace("list_page_", ""))
            await self.show_address_list(query, user_id, page)

        # Back button handlers
        elif data == "back_addr":
            # Go back to the address detail view
            address = context.user_data.get("current_address")
            if address:
                await self.show_address_detail(query, user_id, address, context)
            else:
                await self.show_address_list(query, user_id)
        elif data == "cancel_rm":
            # Cancel remove and go back to address detail
            address = context.user_data.get("current_address")
            if address:
                await self.show_address_detail(query, user_id, address, context)

        # Utility handlers
        elif data == "refresh_all":
            await self.refresh_all_addresses(query, user_id)
        elif data == "noop":
            pass  # Do nothing for placeholder buttons

    async def show_main_menu(self, query) -> None:
        """Show main menu"""
        text = (
            "🎯 *Kaspa Address Tracker*\n\n"
            "Monitor your Kaspa addresses and get real-time transaction notifications.\n\n"
            "Choose an action:"
        )
        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.main_menu_keyboard()
        )

    async def start_add_address(self, query, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start the add address conversation"""
        await query.edit_message_text(
            "➕ *Add New Address*\n\n"
            "Please send the Kaspa address you want to track.\n\n"
            "Example:\n`kaspa:qq258y97v6uc26jqhztw49v9xh6wa85fc8sd5zqxz9jmhkky4pnvvgc3z08eq`",
            parse_mode="Markdown",
            reply_markup=self.ui.cancel_keyboard(),
        )
        context.user_data["adding_address"] = True
        return WAITING_ADDRESS

    async def show_address_list(self, query, user_id: int, page: int = 0) -> None:
        """Show paginated address list"""
        # Show loading message first
        await query.edit_message_text("🔄 Loading addresses...")

        addresses = await self.db.get_user_addresses(user_id)

        if not addresses:
            await query.edit_message_text(
                "📋 *Your Tracked Addresses*\n\n"
                "You haven't added any addresses yet.\n"
                "Click 'Add Address' to start tracking!",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("➕ Add Address", callback_data="menu_add"),
                            InlineKeyboardButton("⬅️ Back", callback_data="menu_main"),
                        ]
                    ]
                ),
            )
            return

        # Format address list
        text = f"📋 *Your Tracked Addresses ({len(addresses)})*\n\n"

        # Add addresses with their info
        per_page = 5
        start = page * per_page
        end = min(start + per_page, len(addresses))

        for i, addr in enumerate(addresses[start:end], start=start + 1):
            addr_short = f"{addr['address'][:12]}...{addr['address'][-6:]}"
            label = addr.get("label", "")

            # Fetch fresh balance from API
            balance = 0
            try:
                balance_data = await self.kaspa_api.get_balance(addr["address"])
                if balance_data:
                    balance = balance_data["balance_kas"]
            except Exception as e:
                logger.error(f"Error fetching balance for {addr_short}: {e}")
                balance = 0

            text += f"*{i}.* `{addr_short}`\n"
            if label:
                text += f"   📌 {label}\n"
            text += f"   💰 {balance:.8f} KAS\n\n"

        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.address_list_keyboard(addresses, page)
        )

    async def show_address_detail(
        self, query, user_id: int, address: str, context: ContextTypes.DEFAULT_TYPE = None
    ) -> None:
        """Show detailed address information"""
        # Show loading message first
        await query.edit_message_text("🔄 Loading address details...")

        # Store current address in context for subsequent actions
        if context:
            context.user_data["current_address"] = address

        # Get address info from database (for label)
        addr_info = await self.db.get_address_info(user_id, address)

        if not addr_info:
            await query.edit_message_text(
                "❌ Address not found in your tracked list.",
                reply_markup=self.ui.back_button("menu_list"),
            )
            return

        # Fetch fresh balance and UTXO data from API
        try:
            balance_data = await self.kaspa_api.get_balance(address)
            utxos = await self.kaspa_api.get_utxos(address)

            # Update addr_info with fresh data
            if balance_data:
                addr_info["balance"] = balance_data["balance_kas"]
            else:
                addr_info["balance"] = 0

            addr_info["utxo_count"] = len(utxos) if utxos else 0
        except Exception as e:
            logger.error(f"Error fetching fresh data for address detail: {e}")
            addr_info["balance"] = 0
            addr_info["utxo_count"] = 0

        # Format and show address details
        text = self.ui.format_address_info(addr_info)

        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=self.ui.address_detail_keyboard(bool(addr_info.get("label"))),
        )

    async def check_balance(self, query, address: str) -> None:
        """Check and show current balance"""
        await query.edit_message_text("🔄 Fetching balance...")

        balance_data = await self.kaspa_api.get_balance(address)

        if balance_data:
            text = (
                f"💰 *Balance Check*\n\n"
                f"Address: `{address[:20]}...`\n"
                f"Balance: {balance_data['balance_kas']:.8f} KAS"
            )
        else:
            text = "❌ Failed to fetch balance. Please try again."

        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.back_button("back_addr")
        )

    async def show_utxos(self, query, address: str) -> None:
        """Show UTXOs for address"""
        await query.edit_message_text("🔄 Fetching UTXOs...")

        utxos = await self.kaspa_api.get_utxos(address)

        if utxos:
            text = f"📦 *UTXOs ({len(utxos)})*\n\n"

            # Show first 10 UTXOs
            for i, utxo in enumerate(utxos[:10], 1):
                amount = utxo.get("amount_kas", 0)
                tx_id = utxo.get("tx_id", "")[:16]
                text += f"{i}. {amount:.8f} KAS\n   `{tx_id}...`\n\n"

            if len(utxos) > 10:
                text += f"... and {len(utxos) - 10} more"
        else:
            text = "❌ No UTXOs found or failed to fetch."

        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.back_button("back_addr")
        )

    async def show_transactions(self, query, address: str) -> None:
        """Show recent transactions"""
        await query.edit_message_text("🔄 Fetching transactions...")

        transactions = await self.kaspa_api.get_transactions(address, limit=10)

        if transactions:
            text = self.ui.format_transaction_list(transactions)
        else:
            text = "❌ No transactions found or failed to fetch."

        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.back_button("back_addr")
        )

    async def confirm_remove(self, query, context: ContextTypes.DEFAULT_TYPE, address: str) -> None:
        """Show removal confirmation"""
        text = (
            f"⚠️ *Confirm Removal*\n\n"
            f"Are you sure you want to stop tracking this address?\n\n"
            f"Address: `{address[:20]}...`\n\n"
            f"This action cannot be undone."
        )

        await query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=self.ui.confirm_remove_keyboard()
        )

    async def remove_address(self, query, user_id: int, address: str) -> None:
        """Remove address from tracking"""
        # Unsubscribe from gRPC notifications
        await self.kaspa_client.unsubscribe_from_address(address)

        # Remove from database
        await self.db.remove_address(user_id, address)

        await query.edit_message_text(
            "✅ Address removed successfully!", reply_markup=self.ui.back_button("menu_list")
        )

    async def refresh_all_addresses(self, query, user_id: int) -> None:
        """Refresh all addresses"""
        await query.edit_message_text("🔄 Fetching fresh balances...")

        addresses = await self.db.get_user_addresses(user_id)

        # Just verify we can reach the API for all addresses
        successful = 0
        for addr in addresses:
            try:
                balance_data = await self.kaspa_api.get_balance(addr["address"])
                if balance_data:
                    successful += 1
            except Exception:
                pass

        await query.edit_message_text(
            f"✅ Successfully fetched {successful}/{len(addresses)} addresses!",
            reply_markup=self.ui.back_button("menu_list"),
        )

    async def start_edit_label(
        self, query, context: ContextTypes.DEFAULT_TYPE, address: str
    ) -> int:
        """Start label edit conversation"""
        context.user_data["editing_label_address"] = address

        await query.edit_message_text(
            f"📝 *Edit Label*\n\n"
            f"Address: `{address[:20]}...`\n\n"
            f"Please send the new label for this address:",
            parse_mode="Markdown",
            reply_markup=self.ui.cancel_keyboard(),
        )

        return WAITING_LABEL
