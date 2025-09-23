#!/usr/bin/env python3
"""
Kaspa Tracker Bot Runner
Run this to start the bot with proper output
"""

import asyncio
import logging
import sys
from datetime import datetime

# Configure logging to show output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

print("=" * 40)
print("KASPA TRACKER BOT STARTING")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 40)
sys.stdout.flush()

try:
    print("✓ Importing bot module...", flush=True)
    from src.bot.bot import main

    print("✓ Bot module loaded", flush=True)
    print("✓ Starting Telegram bot polling...", flush=True)
    print("✓ Press Ctrl+C to stop\n", flush=True)

    # Run the bot
    print("Calling main()...", flush=True)
    main()
    print("main() returned", flush=True)

except KeyboardInterrupt:
    print("\n\n⚡ Bot stopped by user", flush=True)
except Exception as e:
    print(f"\n❌ Error: {e}", flush=True)
    import traceback

    traceback.print_exc()
