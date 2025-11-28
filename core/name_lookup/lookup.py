"""Name lookup functionality."""

from .parser import parse_name
from .apis import query_directory_apis
from .scraper import scrape_social_media

def lookup_name(full_name):
    """Main name lookup function."""
    # Parse name components
    name_parts = parse_name(full_name)
    
    # Query APIs and scrape data
    api_data = query_directory_apis(name_parts)
    social_data = scrape_social_media(name_parts)
    
    return {
        **name_parts,
        **api_data,
        **social_data
    }