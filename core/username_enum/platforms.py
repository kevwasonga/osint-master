"""Platform checking for username enumeration."""

def check_all_platforms(username):
    """Check username across all supported platforms."""
    platforms = {
        "github": check_github(username),
        "twitter": check_twitter(username),
        "linkedin": check_linkedin(username),
        "instagram": check_instagram(username),
        "reddit": check_reddit(username),
        "facebook": check_facebook(username),
        "tiktok": check_tiktok(username),
        "youtube": check_youtube(username),
        "pinterest": check_pinterest(username)
    }
    return platforms

import requests
from utils.http import make_request

def check_github(username):
    """Check GitHub for username."""
    try:
        url = f"https://api.github.com/users/{username}"
        response = make_request(url)
        if response and response.status_code == 200:
            return f"https://github.com/{username}"
        return False
    except:
        return False

def check_twitter(username):
    """Check Twitter/X for username via web scraping."""
    try:
        # Check if profile page exists (returns 200 even for suspended accounts)
        url = f"https://twitter.com/{username}"
        response = make_request(url)
        if response and response.status_code == 200:
            # Check if it's not a "This account doesn't exist" page
            if "This account doesn't exist" not in response.text:
                return url
        return False
    except:
        return False

def check_linkedin(username):
    """Check LinkedIn for username via public profile."""
    try:
        # LinkedIn public profile format
        url = f"https://www.linkedin.com/in/{username}"
        response = make_request(url)
        if response and response.status_code == 200:
            # Check if profile exists (not a 404 page)
            if "Page not found" not in response.text and "Member not found" not in response.text:
                return url
        return False
    except:
        return False

def check_instagram(username):
    """Check Instagram for username via web interface."""
    try:
        # Instagram public profile (no login required for basic check)
        url = f"https://www.instagram.com/{username}/"
        response = make_request(url)
        if response and response.status_code == 200:
            # Check if it's not a "Sorry, this page isn't available" page
            if "Sorry, this page isn" not in response.text:
                return url
        return False
    except:
        return False

def check_reddit(username):
    """Check Reddit for username."""
    try:
        # Reddit user API endpoint (public)
        url = f"https://www.reddit.com/user/{username}/about.json"
        response = make_request(url)
        if response and response.status_code == 200:
            data = response.json()
            if data.get('data') is not None:
                return f"https://www.reddit.com/user/{username}"
        return False
    except:
        return False

def check_facebook(username):
    """Check Facebook for username via public profile."""
    try:
        # Facebook public profile check
        url = f"https://www.facebook.com/{username}"
        response = make_request(url)
        if response and response.status_code == 200:
            # Check if profile exists (not redirected to main page)
            if "facebook.com/?" not in response.url and "Content Not Found" not in response.text:
                return url
        return False
    except:
        return False

def check_tiktok(username):
    """Check TikTok for username."""
    try:
        url = f"https://www.tiktok.com/@{username}"
        response = make_request(url)
        if response and response.status_code == 200:
            if "Couldn't find this account" not in response.text:
                return url
        return False
    except:
        return False

def check_youtube(username):
    """Check YouTube for username/channel."""
    try:
        # Try both username and channel formats
        urls = [
            f"https://www.youtube.com/user/{username}",
            f"https://www.youtube.com/c/{username}",
            f"https://www.youtube.com/@{username}"
        ]
        
        for url in urls:
            response = make_request(url)
            if response and response.status_code == 200:
                if "This channel does not exist" not in response.text:
                    return url
        return False
    except:
        return False

def check_pinterest(username):
    """Check Pinterest for username."""
    try:
        url = f"https://www.pinterest.com/{username}/"
        response = make_request(url)
        if response and response.status_code == 200:
            if "Sorry, we couldn't find that page" not in response.text:
                return url
        return False
    except:
        return False