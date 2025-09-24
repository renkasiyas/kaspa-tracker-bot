# ABOUTME: Telegram bot for tracking Kaspa addresses with real-time updates
# ABOUTME: Uses python-telegram-bot v20+ async API and gRPC connection to Kaspa node

import asyncio
import logging
import re
from typing import Any, Dict, Optional

import aiosqlite
import kaspa
from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from config import (
    ADMIN_IDS,
    BOT_TOKEN,
    LOG_LEVEL,
    MAX_ADDRESSES_PER_USER,
    MIN_TRANSACTION_AMOUNT,
    NOTIFY_ON_ALL_TRANSACTIONS,
)

from ..clients.kaspa_api import KaspaAPI
from ..clients.kaspa_grpc import KaspaGrpcClient
from ..db.database import Database
from ..db.migrations import Migrator
from .bot_callbacks import WAITING_ADDRESS, WAITING_LABEL, CallbackHandlers
from .bot_ui import BotUI
from .formatting import format_kas_amount, format_kas_amount_from_float

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=getattr(logging, LOG_LEVEL)
)
logger = logging.getLogger(__name__)

# Global instances
db = Database()
# Architecture: REST API for data fetching, gRPC for real-time notifications
kaspa_client = KaspaGrpcClient()  # For real-time transaction notifications via gRPC
kaspa_api = KaspaAPI()  # For balance, UTXOs, and transaction history via REST
application_instance = None
ui = BotUI()  # UI handler for interactive elements
callback_handlers = None  # Will be initialized in post_init

# Remove old conversation states (now imported from bot_callbacks)


def validate_kaspa_address(address: str) -> bool:
    """Validate Kaspa address using the kaspa SDK"""
    try:
        return kaspa.Address.validate(address)
    except Exception:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with interactive menu when /start command is issued"""
    user = update.effective_user
    await db.add_user(user.id, user.username, user.first_name)

    welcome_message = (
        f"Welcome {user.first_name}! 👋\n\n"
        "🎯 *Kaspa Address Tracker*\n\n"
        "I'll help you monitor your Kaspa addresses for balance changes and real-time transactions.\n\n"
        "Choose an action from the menu below:"
    )

    await update.message.reply_text(
        welcome_message, parse_mode="Markdown", reply_markup=ui.main_menu_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message when /help command is issued"""
    help_text = (
        "📚 *Kaspa Tracker Bot Commands*\n\n"
        "*Adding Addresses:*\n"
        "`/add <address> [label]` - Track a new Kaspa address\n"
        "Example: `/add kaspa:qr2u4...xyz Mining Wallet`\n\n"
        "*Managing Addresses:*\n"
        "`/list` - Show all your tracked addresses with balances\n"
        "`/check <address or #>` - Get detailed info about an address\n"
        "`/remove <address or #>` - Stop tracking an address\n\n"
        "*Using Index Numbers:*\n"
        "After using `/list`, you can use the index numbers:\n"
        "`/check 1` - Check address #1 from your list\n"
        "`/remove 2` - Remove address #2 from your list\n\n"
        f"ℹ️ You can track up to {MAX_ADDRESSES_PER_USER} addresses\n"
        f"⚡ Real-time notifications via WebSocket connection"
    )

    await update.message.reply_text(help_text, parse_mode="Markdown")


async def add_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a new address to track"""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text(
            "Please provide an address to track.\n" "Usage: `/add <address> [label]`",
            parse_mode="Markdown",
        )
        return

    address = context.args[0].lower()
    label = " ".join(context.args[1:]) if len(context.args) > 1 else None

    # Validate address format
    if not validate_kaspa_address(address):
        await update.message.reply_text(
            "❌ Invalid Kaspa address format.\n"
            "Kaspa addresses start with 'kaspa:' followed by 61 characters."
        )
        return

    # Check if user has reached limit
    address_count = await db.get_address_count(user_id)
    if address_count >= MAX_ADDRESSES_PER_USER:
        await update.message.reply_text(
            f"❌ You've reached the maximum limit of {MAX_ADDRESSES_PER_USER} addresses.\n"
            "Please remove an address before adding a new one."
        )
        return

    # Add address to database
    success = await db.add_address(user_id, address, label)
    if not success:
        await update.message.reply_text("⚠️ You're already tracking this address.")
        return

    # Get initial balance from REST API
    logger.info(f"Fetching balance for {address}")
    balance_data = await kaspa_api.get_balance(address)
    if balance_data:
        balance_kas = balance_data["balance_kas"]
        await db.update_address_stats(
            user_id,
            address,
            str(balance_data["balance"]),
            0,  # Will be updated with UTXO count later
        )
        balance_text = format_kas_amount(balance_data["balance"])
        logger.info(f"Balance fetched: {balance_text}")
    else:
        balance_text = "Unable to fetch"
        balance_kas = 0
        logger.error(f"Failed to fetch balance for {address}")

    # Subscribe to real-time updates for this address
    subscription_success = await kaspa_client.subscribe_to_address(address, handle_kaspa_event)
    if subscription_success:
        logger.info(f"Successfully subscribed to real-time updates for {address}")
    else:
        logger.warning(f"Failed to subscribe to real-time updates for {address}")

    response = f"✅ Now tracking address:\n" f"`{address}`\n"
    if label:
        response += f"Label: {label}\n"
    response += f"Balance: {balance_text}"

    await update.message.reply_text(response, parse_mode="Markdown")


async def list_addresses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all tracked addresses for the user"""
    user_id = update.effective_user.id

    addresses = await db.get_user_addresses(user_id)
    if not addresses:
        await update.message.reply_text(
            "📭 You're not tracking any addresses yet.\n" "Use `/add <address>` to start tracking.",
            parse_mode="Markdown",
        )
        return

    response = "📋 *Your Tracked Addresses:*\n\n"
    for i, addr in enumerate(addresses, 1):
        address_short = f"{addr['address'][:12]}...{addr['address'][-6:]}"

        balance = "Checking..."
        if addr["last_balance"]:
            balance = format_kas_amount(int(addr["last_balance"]))

        response += f"{i}. `{address_short}`"
        if addr["label"]:
            response += f" *{addr['label']}*"
        response += f"\n   💰 {balance}\n"

        if addr["last_utxo_count"]:
            response += f"   📦 UTXOs: {addr['last_utxo_count']}\n"

        response += "\n"

    response += f"\n💡 _Use index numbers with commands:_\n" f"`/check 1` or `/remove 2`"

    await update.message.reply_text(response, parse_mode="Markdown")


async def check_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check detailed information about an address"""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text(
            "Please provide an address or index to check.\n" "Usage: `/check <address or #>`",
            parse_mode="Markdown",
        )
        return

    input_value = context.args[0]

    # Check if input is a number (index)
    if input_value.isdigit():
        index = int(input_value)
        address = await db.get_address_by_index(user_id, index)
        if not address:
            await update.message.reply_text(
                f"❌ Address #{index} not found in your list.\n"
                "Use `/list` to see your addresses.",
                parse_mode="Markdown",
            )
            return
    else:
        address = input_value.lower()
        if not validate_kaspa_address(address):
            await update.message.reply_text("❌ Invalid address format or index number.")
            return

        # Check if user is tracking this address
        user_addresses = await db.get_user_addresses(user_id)
        if not any(a["address"] == address for a in user_addresses):
            await update.message.reply_text(
                "⚠️ You're not tracking this address.\n" "Use `/add` to start tracking it.",
                parse_mode="Markdown",
            )
            return

    # Fetch current data from REST API
    await update.message.reply_text("🔍 Fetching latest data...")

    balance_data = await kaspa_api.get_balance(address)
    utxos = await kaspa_api.get_utxos(address)

    if not balance_data:
        await update.message.reply_text("❌ Failed to fetch address data. Please try again later.")
        return

    # Update database
    utxo_count = len(utxos) if utxos else 0
    await db.update_address_stats(user_id, address, str(balance_data["balance"]), utxo_count)

    # Format response
    response = (
        f"📊 *Address Details*\n\n"
        f"Address: `{address}`\n"
        f"Balance: {format_kas_amount(balance_data['balance'])}\n"
        f"UTXOs: {utxo_count}\n"
    )

    if utxos and utxo_count <= 30:
        response += "\n*UTXO List:*\n"
        for utxo in utxos[:30]:
            response += f"• {format_kas_amount(utxo['amount'])}\n"

    await update.message.reply_text(response, parse_mode="Markdown")


async def remove_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove an address from tracking"""
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text(
            "Please provide an address or index to remove.\n" "Usage: `/remove <address or #>`",
            parse_mode="Markdown",
        )
        return

    input_value = context.args[0]

    # Check if input is a number (index)
    if input_value.isdigit():
        index = int(input_value)
        removed_info = await db.remove_address_by_index(user_id, index)
        if not removed_info:
            await update.message.reply_text(
                f"❌ Address #{index} not found in your list.\n"
                "Use `/list` to see your addresses.",
                parse_mode="Markdown",
            )
            return

        # Extract address from removed_info for unsubscription
        # removed_info format: "label (address)" or "(address)"
        address = removed_info.split("(")[-1].rstrip(")")

        await update.message.reply_text(f"✅ Stopped tracking address #{index}:\n{removed_info}")
    else:
        address = input_value.lower()
        if not validate_kaspa_address(address):
            await update.message.reply_text("❌ Invalid address format or index number.")
            return

        success = await db.remove_address(user_id, address)
        if not success:
            await update.message.reply_text("⚠️ You're not tracking this address.")
            return

        await update.message.reply_text(
            f"✅ Stopped tracking address:\n`{address}`", parse_mode="Markdown"
        )

    # Unsubscribe from address notifications
    await kaspa_client.unsubscribe_from_address(address)


async def db_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Admin command to check database migration status"""
    user_id = update.effective_user.id

    # Check if user is admin
    if not ADMIN_IDS:
        await update.message.reply_text("⚠️ No admins configured. Set ADMIN_IDS in your .env file.")
        return

    if user_id not in ADMIN_IDS:
        await update.message.reply_text("⚠️ This command is for administrators only.")
        logger.warning(f"Unauthorized dbstatus attempt by user {user_id}")
        return

    migrator = Migrator(db.db_path)
    status = await migrator.get_migration_status()

    response = "🗄️ *Database Migration Status*\n\n"
    for version, description, is_applied in status:
        status_emoji = "✅" if is_applied else "⏳"
        response += f"{status_emoji} v{version}: {description}\n"

    # Get database stats
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute("SELECT COUNT(*) FROM users")
        user_count = (await cursor.fetchone())[0]

        cursor = await conn.execute("SELECT COUNT(*) FROM addresses")
        address_count = (await cursor.fetchone())[0]

        cursor = await conn.execute("SELECT COUNT(*) FROM transactions")
        tx_count = (await cursor.fetchone())[0]

    response += f"\n📊 *Database Statistics*\n"
    response += f"Users: {user_count}\n"
    response += f"Addresses: {address_count}\n"
    response += f"Transactions: {tx_count}"

    await update.message.reply_text(response, parse_mode="Markdown")


# Track processed transactions to avoid duplicates
processed_transactions = {}  # Format: {tx_id: timestamp}

# Retry queue for transactions that get 404 errors
transaction_retry_queue = {}  # Format: {tx_id: {address, retry_count, next_retry_time}}


async def process_transaction_with_retry(tx_id: str, address: str, retry_count: int = 0) -> bool:
    """Process a transaction with retry logic for 404 errors"""
    global application_instance
    global processed_transactions

    MAX_RETRIES = 5
    BASE_DELAY = 1.0  # Base delay in seconds

    try:
        # Exponential backoff delay based on retry count
        if retry_count > 0:
            delay = min(BASE_DELAY * (2 ** (retry_count - 1)), 30)  # Cap at 30 seconds
            logger.info(
                f"Retry {retry_count}/{MAX_RETRIES} for tx {tx_id} after {delay:.1f}s delay"
            )
            await asyncio.sleep(delay)

        # Fetch transaction from API
        tx_details = await kaspa_api.get_transaction(tx_id)

        if not tx_details:
            if retry_count < MAX_RETRIES:
                # Schedule retry with exponential backoff
                logger.warning(
                    f"Transaction {tx_id} not found (retry {retry_count + 1}/{MAX_RETRIES})"
                )
                asyncio.create_task(process_transaction_with_retry(tx_id, address, retry_count + 1))
                return False
            else:
                logger.error(f"Transaction {tx_id} not found after {MAX_RETRIES} retries")
                return False

        # Successfully got transaction, process it
        await analyze_and_notify_transaction(tx_id, address, tx_details)
        return True

    except Exception as e:
        logger.error(f"Error processing transaction {tx_id}: {e}")
        if retry_count < MAX_RETRIES:
            asyncio.create_task(process_transaction_with_retry(tx_id, address, retry_count + 1))
        return False


async def analyze_and_notify_transaction(tx_id: str, address: str, tx_details: Dict) -> None:
    """Analyze transaction and send notifications if needed"""
    global application_instance

    try:
        # Analyze transaction to determine type
        inputs = tx_details.get("inputs", [])
        outputs = tx_details.get("outputs", [])

        # Calculate totals for this address
        total_input_from_address = 0
        total_output_to_address = 0

        # Check inputs (what was spent from this address)
        for inp in inputs:
            if inp.get("previous_outpoint_address") == address:
                total_input_from_address += int(inp.get("previous_outpoint_amount", "0"))

        # Check outputs (what was received to this address)
        for out in outputs:
            if out.get("script_public_key_address") == address:
                total_output_to_address += int(out.get("amount", "0"))

        # Determine transaction type based on flows
        net_change = total_output_to_address - total_input_from_address

        # Skip if no actual change for this address
        if net_change == 0:
            logger.info(f"No net change for {address} in transaction {tx_id}")
            return

        # Determine transaction type
        if total_input_from_address > 0 and total_output_to_address > 0:
            # Both input and output - likely sending with change back
            if net_change < 0:
                tx_type = "outgoing"
                amount = abs(net_change)
                emoji = "💸"
                sign = "-"
            else:
                # This shouldn't happen normally but handle it
                tx_type = "self"
                amount = abs(net_change)
                emoji = "🔄"
                sign = ""
        elif total_input_from_address > 0:
            # Only input, no output back to us - full send
            tx_type = "outgoing"
            amount = total_input_from_address
            emoji = "💸"
            sign = "-"
        elif total_output_to_address > 0:
            # Only output, no input from us - incoming
            tx_type = "incoming"
            amount = total_output_to_address
            emoji = "💰"
            sign = "+"
        else:
            # Shouldn't happen
            logger.error(f"Unexpected transaction state for {tx_id}")
            return

        # Check if this is a self-transfer (all inputs and outputs are ours)
        all_addresses = set()
        for inp in inputs:
            all_addresses.add(inp.get("previous_outpoint_address"))
        for out in outputs:
            all_addresses.add(out.get("script_public_key_address"))

        if len(all_addresses) == 1 and address in all_addresses:
            tx_type = "self"
            emoji = "🔄"
            sign = ""
            amount = total_output_to_address  # Show total moved

        # Only notify if amount meets threshold
        if amount / 100_000_000 >= MIN_TRANSACTION_AMOUNT or NOTIFY_ON_ALL_TRANSACTIONS:
            # Find users tracking this address
            users = await db.get_users_by_address(address)

            for user_info in users:
                user_id = user_info["user_id"]
                label = user_info.get("label", "")

                # Build notification
                if tx_type == "incoming":
                    notification = f"{emoji} *Incoming Transaction!*\n"
                elif tx_type == "outgoing":
                    notification = f"{emoji} *Outgoing Transaction!*\n"
                else:  # self
                    notification = f"{emoji} *Self-Transfer!*\n"

                notification += f"Address: `{address[:12]}...{address[-6:]}`"
                if label:
                    notification += f" ({label})"
                notification += f"\nAmount: {sign}{format_kas_amount(amount)}\n"
                notification += f"TX: `{tx_id[:12]}...`"

                try:
                    await application_instance.bot.send_message(
                        user_id, notification, parse_mode="Markdown"
                    )

                    # Log transaction
                    await db.add_transaction(
                        user_id,
                        address,
                        tx_type,
                        str(amount),
                        {"tx_id": tx_id, "net_change": net_change},
                    )
                except Exception as e:
                    logger.error(f"Failed to send notification to {user_id}: {e}")

    except Exception as e:
        logger.error(f"Error analyzing transaction {tx_id}: {e}")


async def handle_kaspa_event(event_type: str, address: Optional[str], data: Dict) -> None:
    """Handle events from Kaspa gRPC stream"""
    global application_instance
    global processed_transactions
    global transaction_retry_queue

    import random

    # Only log new_block events 1% of the time to reduce spam
    if event_type == "new_block":
        if random.random() <= 0.01:
            logger.info(f"Received Kaspa event: {event_type} with data: {data}")
    elif address:
        logger.info(
            f"Received Kaspa event: {event_type} for address {address[:20]}... with data: {data}"
        )
    else:
        logger.info(f"Received Kaspa event: {event_type} with data: {data}")

    # Clean old processed transactions (older than 5 minutes)
    import time

    current_time = time.time()
    processed_transactions = {
        tx_id: timestamp
        for tx_id, timestamp in processed_transactions.items()
        if current_time - timestamp < 300
    }

    if event_type == "utxo_added" or event_type == "utxo_removed":
        # UTXO change detected - fetch full transaction to determine type
        tx_id = data.get("tx_id", "unknown")

        # Create unique transaction key (without address to dedupe across all addresses)
        tx_key = f"tx_{tx_id}"

        # Skip if we've already processed this transaction recently
        if tx_key in processed_transactions:
            # Check if it's been at least 10 seconds (to allow retry for 404s)
            if current_time - processed_transactions[tx_key] < 10:
                logger.debug(f"Skipping recently processed transaction: {tx_key}")
                return

        # Mark as processing
        processed_transactions[tx_key] = current_time

        # For removed UTXOs, store them temporarily to match with added UTXOs
        if event_type == "utxo_removed":
            removed_key = f"removed_{tx_id}:{address}"
            processed_transactions[removed_key] = current_time
            logger.info(f"Marked UTXO removal for {address} in tx {tx_id}")

            # Don't process removals directly, wait for the add event
            # which will have the full transaction context
            return

        # For added UTXOs, process the transaction with retry logic
        # Start processing (will retry if needed)
        asyncio.create_task(process_transaction_with_retry(tx_id, address))

    elif event_type == "new_block":
        # New block mined - we don't need to update balances here
        # UTXO changes are already tracked via gRPC notifications
        pass


async def update_all_balances() -> None:
    """Update balances for all tracked addresses"""
    try:
        addresses = await db.get_all_tracked_addresses()

        for addr_info in addresses:
            address = addr_info["address"]
            user_id = addr_info["user_id"]

            # Fetch current balance from REST API
            balance_data = await kaspa_api.get_balance(address)
            if balance_data:
                utxos = await kaspa_api.get_utxos(address)
                utxo_count = len(utxos) if utxos else 0

                await db.update_address_stats(
                    user_id, address, str(balance_data["balance"]), utxo_count
                )
    except Exception as e:
        logger.error(f"Error updating balances: {e}")


async def post_init(application: Application) -> None:
    """Initialize database and Kaspa connection after bot starts"""
    global application_instance, callback_handlers
    application_instance = application

    # Initialize database first
    await db.init_db()
    logger.info("Database initialized")

    # Initialize callback handlers
    callback_handlers = CallbackHandlers(db, kaspa_api, kaspa_client)
    logger.info("Callback handlers initialized")

    # Start Kaspa connection in background (non-blocking)
    asyncio.create_task(init_kaspa_connection())
    logger.info("Bot initialization complete")


async def init_kaspa_connection():
    """Initialize Kaspa connection in background"""
    try:
        # Connect to Kaspa node
        connected = await kaspa_client.connect()
        if not connected:
            logger.error("Failed to connect to Kaspa node")
            return

        logger.info("Connected to Kaspa node")

        # Re-subscribe to all existing addresses from database
        await resubscribe_all_addresses()

    except Exception as e:
        logger.error(f"Error initializing Kaspa connection: {e}")


async def resubscribe_all_addresses():
    """Re-subscribe to all addresses in the database on startup"""
    try:
        # Get all addresses from database
        addresses = await db.get_all_tracked_addresses()

        if not addresses:
            logger.info("No addresses to subscribe to on startup")
            return

        # Get unique addresses (since multiple users can track same address)
        unique_addresses = set()
        for addr_info in addresses:
            unique_addresses.add(addr_info["address"])

        logger.info(f"Re-subscribing to {len(unique_addresses)} addresses on startup...")

        # Subscribe to each address
        successful = 0
        for address in unique_addresses:
            success = await kaspa_client.subscribe_to_address(address, handle_kaspa_event)
            if success:
                successful += 1
                logger.info(f"✅ Re-subscribed to {address[:20]}...")
            else:
                logger.warning(f"Failed to re-subscribe to {address[:20]}...")

        logger.info(
            f"Startup subscription complete - monitoring {successful}/{len(unique_addresses)} addresses"
        )

    except Exception as e:
        logger.error(f"Error re-subscribing to addresses: {e}")


async def post_shutdown(application: Application) -> None:
    """Clean shutdown"""
    await kaspa_client.disconnect()
    logger.info("Disconnected from Kaspa node")


async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Delegate callback query handling to CallbackHandlers"""
    if callback_handlers:
        await callback_handlers.handle_callback(update, context)
    else:
        logger.error("Callback handlers not initialized")


async def handle_label_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle label edit callback to start conversation"""
    query = update.callback_query
    await query.answer()

    # Get the current address from context
    address = context.user_data.get("current_address")
    if not address:
        await query.edit_message_text("❌ Error: Address not found in context")
        return ConversationHandler.END

    # Set up for label editing
    context.user_data["editing_label_address"] = address

    # Store message ID to delete later
    context.user_data["label_prompt_msg_id"] = query.message.message_id

    await query.edit_message_text(
        f"📝 *Edit Label*\n\n"
        f"Address: `{address[:20]}...`\n\n"
        f"Please send the new label for this address:",
        parse_mode="Markdown",
        reply_markup=ui.cancel_keyboard(),
    )

    return WAITING_LABEL


async def handle_add_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle add address callback to start conversation"""
    if callback_handlers:
        return await callback_handlers.handle_callback(update, context)
    else:
        logger.error("Callback handlers not initialized")
        return ConversationHandler.END


async def handle_add_address_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle address input during conversation"""
    if not context.user_data.get("adding_address"):
        return ConversationHandler.END

    user_id = update.effective_user.id
    address = update.message.text.lower().strip()

    # Validate address
    if not validate_kaspa_address(address):
        await update.message.reply_text(
            "❌ Invalid Kaspa address format.\n" "Please send a valid address or click Cancel.",
            reply_markup=ui.cancel_keyboard(),
        )
        return WAITING_ADDRESS

    # Store address and ask for label
    context.user_data["pending_address"] = address
    context.user_data["adding_address"] = False
    context.user_data["adding_label"] = True

    await update.message.reply_text(
        "📝 Would you like to add a label for this address?\n" "Send a label or click Skip.",
        reply_markup=ui.add_label_keyboard(),
    )
    return WAITING_LABEL


async def handle_label_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle label input during conversation"""
    if context.user_data.get("adding_label"):
        user_id = update.effective_user.id
        address = context.user_data.get("pending_address")
        label = update.message.text.strip()

        # Add address with label
        await db.add_address(user_id, address, label)

        # Subscribe to real-time updates
        await kaspa_client.subscribe_to_address(address, handle_kaspa_event)

        await update.message.reply_text(
            f"✅ Address added successfully!\n" f"Label: {label}",
            reply_markup=ui.main_menu_keyboard(),
        )

        # Clean up user data
        context.user_data.pop("pending_address", None)
        context.user_data.pop("adding_label", None)

    elif context.user_data.get("editing_label_address"):
        user_id = update.effective_user.id
        address = context.user_data.get("editing_label_address")
        label = update.message.text.strip()

        # Update label
        await db.update_address_label(user_id, address, label)

        await update.message.reply_text(
            f"✅ Label updated successfully!", reply_markup=ui.back_button("menu_list")
        )

        # Clean up user data
        context.user_data.pop("editing_label_address", None)

    return ConversationHandler.END


async def handle_cancel_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle cancel button in conversations"""
    query = update.callback_query
    await query.answer()

    # Clean up user data
    context.user_data.clear()

    # Show main menu
    await query.edit_message_text(
        "🎯 *Kaspa Address Tracker*\n\n" "Choose an action:",
        parse_mode="Markdown",
        reply_markup=ui.main_menu_keyboard(),
    )

    return ConversationHandler.END


def main() -> None:
    """Start the bot"""
    print(f"Starting Kaspa Tracker Bot...")
    print(f"Bot token: {BOT_TOKEN[:10]}...")

    # Create application
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    # Create conversation handlers for multi-step interactions
    add_conv_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(handle_add_callback, pattern="^menu_add$"),
            CallbackQueryHandler(handle_label_callback, pattern="^addr_lbl_$"),
            CommandHandler("add", add_address),
        ],
        states={
            WAITING_ADDRESS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_add_address_message)
            ],
            WAITING_LABEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_label_message)],
        },
        fallbacks=[CallbackQueryHandler(handle_cancel_callback, pattern="^menu_main$")],
        allow_reentry=True,
    )

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_addresses))
    application.add_handler(CommandHandler("check", check_address))
    application.add_handler(CommandHandler("remove", remove_address))
    application.add_handler(CommandHandler("dbstatus", db_status))

    # Add conversation handler for multi-step interactions (needs to be before general callback handler)
    application.add_handler(add_conv_handler)

    # Add callback query handler for all other button interactions (lower priority)
    application.add_handler(CallbackQueryHandler(handle_callback_query), group=1)

    print("Bot handlers registered")

    # Start bot
    logger.info("Starting bot polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
