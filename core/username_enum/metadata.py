"""Metadata fetching for username enumeration."""

def fetch_metadata(username, platform_results):
    """Fetch metadata for found usernames."""
    metadata = {}
    
    for platform, found in platform_results.items():
        if found:
            metadata[platform] = get_platform_metadata(platform, username)
    
    return metadata

def get_platform_metadata(platform, username):
    """Get metadata for specific platform."""
    # Placeholder for platform-specific metadata fetching
    return {
        "bio": None,
        "followers": None,
        "activity": None
    }