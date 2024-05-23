# Currency Price Bot

This project is a Python-based application that fetches real-time currency prices from the Navasan website and sends the latest rates to a Telegram channel or user via a Telegram bot.

## Features

- **Real-Time Data**: Retrieves current currency prices from Navasan.net using Selenium and BeautifulSoup.
- **Telegram Integration**: Sends updates directly to a Telegram bot, making it easy to receive notifications on your phone or computer.
- **Localized Timing**: Includes conversion to Shamsi (Persian) date and local time in Iran.
- **Error Handling**: Basic error handling for network failures or API errors.
- **Logging**: Logs activities and errors for easy troubleshooting and monitoring.

## Requirements

- Python 3.6+
- `selenium` library
- `beautifulsoup4` library
- `requests` library
- `pytz` library
- `jdatetime` library
- Google Chrome
- ChromeDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/currency-price-bot.git
   cd currency-price-bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install [Google Chrome](https://www.google.com/chrome/).

4. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) that matches your Chrome version and place it in a directory of your choice.

5. Set up your Telegram bot:
   - Create a new bot via [BotFather](https://core.telegram.org/bots#botfather) and obtain the API token.
   - Update the configuration variables in the script (`CHROME_DRIVER_PATH`, `TELEGRAM_BOT_TOKEN`, and `TELEGRAM_CHAT_ID`) with your values.

## Usage

1. Update the script with your configuration values:
   ```python
   CHROME_DRIVER_PATH = "path_to_your_chromedriver"
   TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
   TELEGRAM_CHAT_ID = "your_telegram_chat_id"
   ```

2. Run the bot:
   ```bash
   python3 main.py
   ```

The bot will start fetching currency prices and send updates to the configured Telegram chat.

## Configuration

The main script requires the following constants to be set:
- `CHROME_DRIVER_PATH`: Path to your ChromeDriver executable.
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID where the messages will be sent.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## Acknowledgements

- [Selenium](https://www.selenium.dev/) for browser automation.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing HTML.
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the Telegram bot API wrapper.
- [requests](https://docs.python-requests.org/en/master/) for HTTP requests.
- [jdatetime](https://github.com/slashmili/python-jalali) for converting Gregorian dates to Shamsi.
