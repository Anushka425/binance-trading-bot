# Binance Trading Bot

A simplified Python trading application for Binance Futures Testnet.

## Setup Steps
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your Binance Testnet API credentials as environment variables or replace them in `bot/cli.py`.

## How to Run Examples
- MARKET Order:
  `python -m bot.cli --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001`
- LIMIT Order:
  `python -m bot.cli --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 60000`

## Assumptions
- This application exclusively interacts with the Binance Futures Testnet base URL.
- The application assumes a structured environment where the `bot` package is accessible.
