"""Database utilities for network analysis application."""
import os
import logging
from datetime import datetime

# Configure logging
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'app.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_packet_analysis(source_ip, destination_ip, protocol, packet_data):
    """Log packet analysis event."""
    logger.info(f"Packet analysis: {source_ip} -> {destination_ip} ({protocol})")
    return {
        'timestamp': datetime.now().isoformat(),
        'source_ip': source_ip,
        'destination_ip': destination_ip,
        'protocol': protocol
    }

def log_user_login(username):
    """Log user login event."""
    logger.info(f"User login: {username}")

def log_api_call(endpoint, method, status_code):
    """Log API call event."""
    logger.info(f"API call: {method} {endpoint} - Status: {status_code}")

if __name__ == '__main__':
    logger.info("Database utilities module initialized")
