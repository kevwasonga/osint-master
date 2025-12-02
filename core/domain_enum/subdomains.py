"""Subdomain discovery functionality."""

def discover_subdomains(domain):
    """Discover subdomains using various methods."""
    subdomains = []
    
    # Certificate Transparency logs
    ct_subdomains = query_certificate_transparency(domain)
    subdomains.extend(ct_subdomains)
    
    # DNS brute force (common subdomains)
    brute_subdomains = brute_force_subdomains(domain)
    subdomains.extend(brute_subdomains)
    
    return list(set(subdomains))  # Remove duplicates

import requests
from utils.http import make_request

def query_certificate_transparency(domain):
    """Query Certificate Transparency logs."""
    try:
        # Using crt.sh API
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = make_request(url)
        
        if response and response.status_code == 200:
            data = response.json()
            subdomains = set()
            
            for cert in data:
                name_value = cert.get('name_value', '')
                for name in name_value.split('\n'):
                    if name.endswith(f'.{domain}'):
                        subdomains.add(name)
            
            return list(subdomains)[:10]  # Limit results
    except Exception as e:
        print(f"Certificate Transparency lookup failed: {e}")
    
    return []

def brute_force_subdomains(domain):
    """Brute force common subdomains."""
    common_subs = ['www', 'mail', 'ftp', 'admin', 'api', 'dev', 'test', 'staging']
    found_subs = []
    
    for sub in common_subs:
        subdomain = f"{sub}.{domain}"
        try:
            # Simple DNS resolution check
            import socket
            socket.gethostbyname(subdomain)
            found_subs.append(subdomain)
        except:
            pass
    
    return found_subs