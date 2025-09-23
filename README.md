# Kaspa Tracker Bot

A Telegram bot for tracking Kaspa blockchain addresses with real-time notifications.

**Bot:** [@kaspa_tracker_bot](https://t.me/kaspa_tracker_bot)

## Features

- =� **Real-time Balance Tracking** - Monitor multiple Kaspa addresses simultaneously
- = **Instant Notifications** - Get alerts for incoming and outgoing transactions
- <� **Custom Labels** - Organize your addresses with descriptive names
- =� **Transaction History** - View recent transactions for any tracked address
- <� **Interactive UI** - Easy-to-use button interface, no commands to memorize

## Getting Started

1. Start a chat with [@kaspa_tracker_bot](https://t.me/kaspa_tracker_bot)
2. Send `/start` to begin
3. Click "� Add Address" to track your first Kaspa address
4. Receive real-time notifications when transactions occur

## How to Use

### Adding an Address
- Click "� Add Address" from the main menu
- Send your Kaspa address (starts with `kaspa:`)
- Optionally add a label to identify the address

### Managing Addresses
- Click "=� My Addresses" to view all tracked addresses
- Select any address to:
  - View current balance
  - See recent transactions
  - Edit the label
  - Remove from tracking

### Notifications
The bot automatically monitors your addresses and sends notifications for:
- Incoming transactions (received KAS)
- Outgoing transactions (sent KAS)

## Self-Hosting

### Requirements
- Python 3.12+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### Quick Start

#### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/yourusername/kaspa-tracker.git
cd kaspa-tracker
```

2. Create `.env` file:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

3. Run with Docker Compose:
```bash
docker-compose up -d
```

#### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/kaspa-tracker.git
cd kaspa-tracker
```

2. Install dependencies with uv:
```bash
pip install uv
uv sync
```

3. Set your bot token:
```bash
export TELEGRAM_BOT_TOKEN=your_bot_token_here
```

4. Run the bot:
```bash
uv run python run.py
```

### Configuration

The bot stores data in a local SQLite database (`kaspa_tracker.db`). When using Docker, this is persisted in a `data/` volume.

### Building from Source

```bash
# Build Docker image
docker-compose build

# Or build directly
docker build -t kaspa-tracker .
```

## Privacy & Security

- The bot only stores Kaspa addresses and user preferences
- No private keys or sensitive data are ever requested or stored
- Each user can only see and manage their own addresses
- Database is stored locally (not shared with any external service)

## Technical Details

- Built with Python and python-telegram-bot
- Real-time monitoring via gRPC connection to Kaspa nodes
- REST API integration for balance and transaction data
- SQLite database for persistent storage
- Async architecture for optimal performance

## Support

For issues or questions, please open an issue on GitHub or contact the bot administrator.

## License

MIT License - See LICENSE file for details