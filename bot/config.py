import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')
TESTNET_BASE_URL = os.getenv('TESTNET_BASE_URL', 'https://testnet.binancefuture.com')
