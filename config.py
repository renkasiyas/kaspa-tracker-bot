# ABOUTME: Configuration module for environment variables and settings
# ABOUTME: Loads bot token and other settings from environment or .env file

import os

from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

# Kaspa Node Configuration
KASPA_WS_URL = os.getenv("KASPA_WS_URL", "ws://mainnet.kasanova.io:18110")

# Database Configuration
DATABASE_PATH = os.getenv("DATABASE_PATH", "kaspa_tracker.db")

# User Limits
MAX_ADDRESSES_PER_USER = int(os.getenv("MAX_ADDRESSES_PER_USER", "20"))

# Admin Configuration
ADMIN_IDS = os.getenv("ADMIN_IDS", "").split(",") if os.getenv("ADMIN_IDS") else []
ADMIN_IDS = [int(id.strip()) for id in ADMIN_IDS if id.strip().isdigit()]

# Notification Settings
MIN_TRANSACTION_AMOUNT = float(os.getenv("MIN_TRANSACTION_AMOUNT", "0"))  # KAS
NOTIFY_ON_ALL_TRANSACTIONS = os.getenv("NOTIFY_ON_ALL_TRANSACTIONS", "true").lower() == "true"

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
