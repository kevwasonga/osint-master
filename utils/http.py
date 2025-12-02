"""HTTP utilities for API requests and web scraping."""

import requests
import time
import random
from config.settings import API_TIMEOUT, RATE_LIMIT_DELAY, USER_AGENT

# Common browser user agents to avoid detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
]

def make_request(url, headers=None, timeout=None, allow_redirects=True):
    """Make HTTP request with rate limiting and error handling."""
    if headers is None:
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
    
    if timeout is None:
        timeout = API_TIMEOUT
    
    try:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=allow_redirects)
        return response  # Don't raise for status, let caller handle
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None