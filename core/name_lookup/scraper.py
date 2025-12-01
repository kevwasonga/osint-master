"""Social media scraping for name lookup."""

def scrape_social_media(name_parts):
    """Scrape social media for name information."""
    first_name = name_parts.get('first_name', '').lower()
    last_name = name_parts.get('last_name', '').lower()
    
    # Mock social media data (replace with real scraping)
    social_data = {
        "social_media": {
            "linkedin": None,
            "facebook": None,
            "twitter": None
        }
    }
    
    if first_name and last_name:
        # Generate likely social media URLs
        social_data["social_media"] = {
            "linkedin": f"linkedin.com/in/{first_name}{last_name}",
            "facebook": f"facebook.com/{first_name}.{last_name}",
            "twitter": f"twitter.com/{first_name}_{last_name}"
        }
    
    return social_data