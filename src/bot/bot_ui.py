# ABOUTME: Interactive UI components for Kaspa Tracker Bot
# ABOUTME: Provides inline keyboards, buttons, and callback handlers

import logging
from typing import Any, Dict, List, Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Import formatting functions
from .formatting import format_kas_amount, format_kas_amount_from_float

logger = logging.getLogger(__name__)


class BotUI:
    """Handles all UI components and interactions"""

    @staticmethod
    def main_menu_keyboard() -> InlineKeyboardMarkup:
        """Create main menu keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("➕ Add Address", callback_data="menu_add"),
                InlineKeyboardButton("📋 My Addresses", callback_data="menu_list"),
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def address_list_keyboard(
        addresses: List[Dict], page: int = 0, per_page: int = 5
    ) -> InlineKeyboardMarkup:
        """Create paginated address list keyboard"""
        keyboard = []

        # Calculate pagination
        total = len(addresses)
        start = page * per_page
        end = min(start + per_page, total)
        total_pages = (total + per_page - 1) // per_page

        # Add address buttons (show first 5 per page)
        for i, addr in enumerate(addresses[start:end], start=start + 1):
            addr_short = f"{addr['address'][:12]}...{addr['address'][-6:]}"
            label = f" ({addr.get('label', '')})" if addr.get("label") else ""
            button_text = f"{i}. {addr_short}{label}"
            # Use index instead of full address for callback data
            keyboard.append([InlineKeyboardButton(button_text, callback_data=f"addr_v_{i-1}")])

        # Add navigation row
        nav_row = []
        if page > 0:
            nav_row.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"list_page_{page-1}"))
        nav_row.append(InlineKeyboardButton(f"📄 {page+1}/{total_pages}", callback_data="noop"))
        if page < total_pages - 1:
            nav_row.append(InlineKeyboardButton("Next ➡️", callback_data=f"list_page_{page+1}"))

        if nav_row:
            keyboard.append(nav_row)

        # Add action buttons
        keyboard.append(
            [
                InlineKeyboardButton("➕ Add New", callback_data="menu_add"),
                InlineKeyboardButton("🔄 Refresh All", callback_data="refresh_all"),
            ]
        )
        keyboard.append([InlineKeyboardButton("⬅️ Back to Menu", callback_data="menu_main")])

        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def address_detail_keyboard(has_label: bool = False) -> InlineKeyboardMarkup:
        """Create address detail view keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("💰 Check Balance", callback_data="addr_bal_"),
                InlineKeyboardButton("📊 View UTXOs", callback_data="addr_utxo_"),
            ],
            [
                InlineKeyboardButton("📜 Recent TXs", callback_data="addr_tx_"),
                InlineKeyboardButton(
                    "✏️ Edit Label" if has_label else "📝 Add Label", callback_data="addr_lbl_"
                ),
            ],
            [
                InlineKeyboardButton("🗑 Remove", callback_data="addr_rm_"),
                InlineKeyboardButton("⬅️ Back to List", callback_data="menu_list"),
            ],
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def confirm_remove_keyboard() -> InlineKeyboardMarkup:
        """Create confirmation dialog for address removal"""
        keyboard = [
            [
                InlineKeyboardButton("✅ Yes, Remove", callback_data="confirm_rm"),
                InlineKeyboardButton("❌ Cancel", callback_data="cancel_rm"),
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def transaction_keyboard(tx_id: str, address: str) -> InlineKeyboardMarkup:
        """Create transaction notification keyboard"""
        keyboard = [
            [
                InlineKeyboardButton(
                    "📋 View Details", url=f"https://explorer.kaspa.org/txs/{tx_id}"
                ),
                InlineKeyboardButton("📊 View Address", callback_data=f"addr_view_{address}"),
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def add_label_keyboard() -> InlineKeyboardMarkup:
        """Create keyboard for adding/editing label"""
        keyboard = [
            [
                InlineKeyboardButton("📝 Set Label", callback_data="set_lbl"),
                InlineKeyboardButton("⏭ Skip", callback_data="skip_lbl"),
            ]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def cancel_keyboard() -> InlineKeyboardMarkup:
        """Create cancel button for operations"""
        keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data="menu_main")]]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def back_button(callback_data: str = "menu_main") -> InlineKeyboardMarkup:
        """Create a simple back button"""
        # Ensure callback_data doesn't exceed 64 bytes
        if len(callback_data) > 60:
            callback_data = "menu_main"
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data=callback_data)]]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def format_address_info(address_data: Dict) -> str:
        """Format address information for display"""
        address = address_data.get("address", "Unknown")
        label = address_data.get("label", "")
        # Use fresh balance fetched from API
        balance = address_data.get("balance", 0)
        utxo_count = address_data.get("utxo_count", 0)

        text = f"📊 *Address Details*\n\n"
        if label:
            text += f"📌 Label: {label}\n"
        text += f"🏠 Address:\n`{address}`\n\n"
        text += f"💰 Balance: {format_kas_amount_from_float(balance)}\n"
        text += f"📦 UTXOs: {utxo_count}\n"

        return text

    @staticmethod
    def format_transaction_list(transactions: List[Dict], limit: int = 5) -> str:
        """Format transaction list for display"""
        if not transactions:
            return "📜 *Recent Transactions*\n\nNo transactions found."

        from datetime import datetime

        text = "📜 *Recent Transactions*\n\n"
        for i, tx in enumerate(transactions[:limit], 1):
            tx_id = tx.get("transaction_id", "Unknown")
            tx_type = tx.get("transaction_type", "unknown")
            amount = int(tx.get("amount", 0))
            timestamp_ms = tx.get("timestamp", 0)

            # Convert milliseconds timestamp to readable format
            if timestamp_ms and timestamp_ms > 0:
                dt = datetime.fromtimestamp(timestamp_ms / 1000)
                timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            else:
                timestamp_str = "Unknown"

            if tx_type == "incoming":
                emoji = "💰"
                sign = "+"
            elif tx_type == "outgoing":
                emoji = "💸"
                sign = "-"
            else:
                emoji = "🔄"
                sign = ""

            text += f"{i}. {emoji} {sign}{format_kas_amount(amount)}\n"
            text += f"   `{tx_id[:16]}...`\n"
            text += f"   {timestamp_str}\n\n"

        return text
