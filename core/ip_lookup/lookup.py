"""IP lookup functionality."""

from .geolocation import get_geolocation
from .abuse import check_abuse_databases

def lookup_ip(ip_address):
    """Main IP lookup function."""
    geo_data = get_geolocation(ip_address)
    abuse_data = check_abuse_databases(ip_address)
    
    return {
        "ip": ip_address,
        **geo_data,
        **abuse_data
    }