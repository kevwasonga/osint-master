"""Platform checking for username enumeration."""

def check_all_platforms(username):
    """Check username across all supported platforms."""
    platforms = {
        "github": check_github(username),
        "twitter": check_twitter(username),
        "linkedin": check_linkedin(username),
        "instagram": check_instagram(username),
        "reddit": check_reddit(username),
        "facebook": check_facebook(username)
    }
    return platforms

import requests
from utils.http import make_request

def check_github(username):
    """Check GitHub for username."""
    try:
        url = f"https://api.github.com/users/{username}"
        response = make_request(url)
        return response and response.status_code == 200
    except:
        return False

def check_twitter(username):
    """Check Twitter for username."""
    # Mock check (Twitter API requires authentication)
    return len(username) > 3  # Simple mock logic

def check_linkedin(username):
    """Check LinkedIn for username."""
    # Mock check (LinkedIn blocks automated requests)
    return len(username) > 2

def check_instagram(username):
    """Check Instagram for username."""
    # Mock check (Instagram blocks automated requests)
    return len(username) > 4

def check_reddit(username):
    """Check Reddit for username."""
    try:
        url = f"https://www.reddit.com/user/{username}/about.json"
        response = make_request(url)
        return response and response.status_code == 200
    except:
        return False

def check_facebook(username):
    """Check Facebook for username."""
    # Mock check (Facebook blocks automated requests)
    return len(username) > 3