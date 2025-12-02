"""WHOIS lookup functionality."""

from datetime import datetime

def get_whois_data(domain):
    """Get WHOIS data for domain."""
    try:
        import whois
        w = whois.whois(domain)
        return {
            "registrar": w.registrar,
            "creation_date": str(w.creation_date) if w.creation_date else None,
            "expiration_date": str(w.expiration_date) if w.expiration_date else None,
            "name_servers": w.name_servers if w.name_servers else []
        }
    except Exception as e:
        print(f"WHOIS lookup failed: {e}")
        return {
            "registrar": "Unknown",
            "creation_date": None,
            "expiration_date": None,
            "name_servers": []
        }