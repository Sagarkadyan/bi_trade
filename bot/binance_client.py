from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from config import API_KEY, SECRET_KEY, TESTNET_BASE_URL
from logger_config import logger

class BinanceFuturesClient:
    def __init__(self):
        if not API_KEY or not SECRET_KEY:
            logger.error("API_KEY or SECRET_KEY not found in environment variables.")
            raise ValueError("API_KEY and SECRET_KEY must be set in the .env file.")
        
        self.client = Client(API_KEY, SECRET_KEY, testnet=True)
        self.client.futures_url = TESTNET_BASE_URL 

    def _execute_order(self, order_func, symbol, side, order_type, quantity, price=None, timeInForce=None):
        try:
            request_params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }
            if price:
                request_params["price"] = price
            if timeInForce:
                request_params["timeInForce"] = timeInForce

            logger.info(f"Sending order request: {request_params}")
            
            if order_type == "MARKET":
                order = order_func(symbol=symbol, side=side, type=order_type, quantity=quantity)
            elif order_type == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                order = order_func(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price, timeInForce=timeInForce)
            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logger.info(f"Order response received: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error: {e}")
            raise
        except ValueError as e:
            logger.error(f"Order validation error: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred during order placement: {e}")
            raise

    def place_market_order(self, symbol, side, quantity):
        logger.info(f"Attempting to place MARKET order: Symbol={symbol}, Side={side}, Quantity={quantity}")
        return self._execute_order(self.client.futures_create_order, symbol, side, "MARKET", quantity)

    def place_limit_order(self, symbol, side, quantity, price, timeInForce="GTC"):
        logger.info(f"Attempting to place LIMIT order: Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}, TimeInForce={timeInForce}")
        return self._execute_order(self.client.futures_create_order, symbol, side, "LIMIT", quantity, price, timeInForce)

    def get_account_balance(self):
        try:
            logger.info("Fetching account balance...")
            balance = self.client.futures_account_balance()
            logger.info(f"Account balance received: {balance}")
            return balance
        except BinanceAPIException as e:
            logger.error(f"Binance API Error fetching balance: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error fetching balance: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while fetching balance: {e}")
            raise
