"""Subdomain vulnerability checking functionality."""

def check_subdomain_vulnerability(subdomain, signatures):
    """Check if subdomain is vulnerable to takeover."""
    # Get CNAME record
    cname = get_cname_record(subdomain)
    if not cname:
        return None
    
    # Check against signatures
    for provider, sig in signatures.items():
        if is_vulnerable_to_provider(cname, sig):
            return {
                "subdomain": subdomain,
                "provider": provider,
                "cname": cname,
                "risk_level": "high",
                "recommendation": f"Remove DNS record or claim {provider} resource"
            }
    
    return None

import dns.resolver
import requests
from utils.http import make_request

def get_cname_record(subdomain):
    """Get CNAME record for subdomain."""
    try:
        result = dns.resolver.resolve(subdomain, 'CNAME')
        return str(result[0]) if result else None
    except:
        return None

def is_vulnerable_to_provider(cname, signature):
    """Check if CNAME is vulnerable to specific provider."""
    for pattern in signature["cname_patterns"]:
        if pattern in cname:
            # Check if the target responds with error messages
            try:
                response = make_request(f"http://{cname}")
                if response:
                    content = response.text
                    for error_msg in signature["error_messages"]:
                        if error_msg.lower() in content.lower():
                            return True
            except:
                pass
            return True  # CNAME points to provider but may be unclaimed
    return False