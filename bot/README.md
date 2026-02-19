# Binance Futures Testnet Trading Bot

This is a simplified Python application designed to place orders on the Binance Futures Testnet (USDT-M). It provides a clean, reusable structure with proper logging and error handling, and accepts user input via the command-line interface (CLI).

## Features

*   Place Market and Limit orders.
*   Support for BUY and SELL sides.
*   Command-line interface for user input (symbol, side, order type, quantity, price).
*   Structured code with separate client/API and CLI layers.
*   Logging of API requests, responses, and errors to a log file (`trading_bot.log`).
*   Robust exception handling for invalid input, API errors, and network failures.

## Setup

### 1. Prerequisites

*   **Python 3.x**: Ensure you have Python 3 installed.
*   **Binance Futures Testnet Account**:
    *   Register and activate a Binance Futures Testnet account.
    *   Generate API credentials (API Key and Secret Key) for your testnet account.

### 2. Clone the Repository 



### 3. Create a Virtual Environment 

Navigate to the project directory in your terminal and create a virtual environment:

```bash
python3 -m venv bot_env
```

Activate the virtual environment:


### 4. Install Dependencies

With your virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

Create a file named `.env` in the root directory of the project (where `main.py` is located) and add your Binance Futures Testnet API Key and Secret Key:

```
BINANCE_API_KEY='YOUR_BINANCE_TESTNET_API_KEY'
BINANCE_SECRET_KEY='YOUR_BINANCE_TESTNET_SECRET_KEY'
TESTNET_BASE_URL='https://testnet.binancefuture.com'
```

**Replace `YOUR_BINANCE_TESTNET_API_KEY` and `YOUR_BINANCE_TESTNET_SECRET_KEY` with your actual testnet credentials.**

## How to Run

The application is run via the `main.py` script, which acts as the entry point for the CLI.

### General Usage

```bash
python main.py --symbol <SYMBOL> --side <BUY/SELL> --type <MARKET/LIMIT> --quantity <QUANTITY> [--price <PRICE_FOR_LIMIT>]
```

### Examples
#### Note: Futures orders must meet minimum notional requirements (~100 USDT on testnet)

So at least use --quantity 0.002 
#### 1. Place a MARKET BUY Order

This example places a market buy order for 0.001 BTC on BTCUSDT.

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

#### 2. Place a MARKET SELL Order

This example places a market sell order for 0.001 BTC on BTCUSDT.

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

#### 3. Place a LIMIT BUY Order

This example places a limit buy order for 0.001 BTC on BTCUSDT at a price of 60000.

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

#### 4. Place a LIMIT SELL Order

This example places a limit sell order for 0.001 BTC on BTCUSDT at a price of 65000.

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

## Log Files

All API requests, responses, and errors are logged to `logs/trading_bot.log`. After running the examples, you can check this file for detailed information.

## Assumptions

*   You have a working internet connection.
*   Your Binance Futures Testnet API keys have the necessary permissions to place orders.
*   The `TESTNET_BASE_URL` is correctly configured in your `.env` file.
*   The symbols and prices used in examples are for demonstration purposes. Always verify current market conditions and available symbols on the Binance Futures Testnet.

## Lightweight UI

The application provides a lightweight UI through its command-line output, summarizing the order request and displaying the order response details, along with success/failure messages. All interactions are text-based via the terminal.
