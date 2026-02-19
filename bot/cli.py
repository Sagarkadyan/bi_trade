import argparse
from binance_client import BinanceFuturesClient
from logger_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Order side (BUY/SELL)")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="Order type (MARKET/LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Quantity of the asset to trade")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders (required for LIMIT type)")

    args = parser.parse_args()

    client = BinanceFuturesClient()

    # Validate price for LIMIT orders
    if args.type == "LIMIT" and args.price is None:
        logger.error("Error: --price is required for LIMIT orders.")
        parser.error("--price is required for LIMIT orders.")
    if args.type == "MARKET" and args.price is not None:
        logger.warning("Warning: --price is ignored for MARKET orders.")

    try:
        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price: {args.price}")
        print("-----------------------------\\n")

        if args.type == "MARKET":
            order_response = client.place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )
        elif args.type == "LIMIT":
            order_response = client.place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )
        
        print("\n--- Order Response Details ---")
        print(f"Order ID: {order_response.get('orderId')}")
        print(f"Status: {order_response.get('status')}")
        print(f"Executed Quantity: {order_response.get('executedQty')}")
        print(f"Average Price: {order_response.get('avgPrice', 'N/A')}")
        print("------------------------------\n")
        print("SUCCESS: Order placed successfully!")

    except ValueError as ve:
        print(f"FAILURE: Invalid input - {ve}")
        logger.error(f"CLI input error: {ve}")
    except Exception as e:
        print(f"FAILURE: An error occurred - {e}")
        logger.error(f"Application error: {e}")

    # Optionally, print account balance after order
    try:
        balance_info = client.get_account_balance()
        usdt_balance = next((item for item in balance_info if item["asset"] == "USDT"), None)
        if usdt_balance:
            print(f"\nCurrent USDT Balance: {usdt_balance['balance']}")
        else:
            print("\nUSDT balance not found.")
    except Exception as e:
        logger.error(f"Could not fetch account balance: {e}")
        print(f"\nCould not fetch account balance: {e}")

if __name__ == "__main__":
    main()
