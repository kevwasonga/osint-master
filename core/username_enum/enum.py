"""Username enumeration functionality."""

from .platforms import check_all_platforms
from .metadata import fetch_metadata

def enumerate_username(username):
    """Main username enumeration function."""
    clean_username = username.lstrip('@')
    
    platform_results = check_all_platforms(clean_username)
    metadata = fetch_metadata(clean_username, platform_results)
    
    return {
        "username": clean_username,
        "platforms": platform_results,
        "metadata": metadata
    }