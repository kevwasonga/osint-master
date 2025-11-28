"""Logging utilities."""

import logging
import os
from datetime import datetime
from config.settings import LOG_LEVEL

def setup_logging():
    """Setup logging configuration."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"osint-master-{datetime.now().strftime('%Y%m%d')}.log")
    
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)