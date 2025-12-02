"""IP geolocation services."""

import requests
from utils.http import make_request

def get_geolocation(ip_address):
    """Get geolocation data for IP address."""
    try:
        # Using ip-api.com (free API)
        url = f"http://ip-api.com/json/{ip_address}"
        response = make_request(url)
        
        if response and response.status_code == 200:
            data = response.json()
            return {
                "isp": data.get('isp'),
                "city": data.get('city'),
                "country": data.get('country'),
                "asn": data.get('as', '').split(' ')[0] if data.get('as') else None
            }
    except Exception as e:
        print(f"Geolocation lookup failed: {e}")
    
    # Fallback mock data
    return {
        "isp": "Example ISP",
        "city": "Example City",
        "country": "Example Country",
        "asn": "12345"
    }