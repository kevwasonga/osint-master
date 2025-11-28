"""HTTP utilities for API requests."""

import requests
import time
from config.settings import API_TIMEOUT, RATE_LIMIT_DELAY, USER_AGENT

def make_request(url, headers=None, timeout=None):
    """Make HTTP request with rate limiting and error handling."""
    if headers is None:
        headers = {"User-Agent": USER_AGENT}
    
    if timeout is None:
        timeout = API_TIMEOUT
    
    try:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None