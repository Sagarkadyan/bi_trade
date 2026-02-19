import logging
import os

def setup_logging():
    log_file = 'trading_bot.log'
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_path = os.path.join('logs', log_file)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler() # Also output to console
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()
