"""Configuration settings for OSINT-Master."""

import os

# API Configuration
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))
RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "1.0"))
USER_AGENT = os.getenv("USER_AGENT", "OSINT-Master/1.0.0 (Educational Tool)")

# API Keys
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Output Configuration
DEFAULT_OUTPUT_FORMAT = os.getenv("DEFAULT_OUTPUT_FORMAT", "txt")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

# Security Settings
MAX_REQUESTS_PER_MINUTE = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "60"))
ENABLE_CACHING = os.getenv("ENABLE_CACHING", "true").lower() == "true"