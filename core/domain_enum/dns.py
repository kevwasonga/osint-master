"""DNS record resolution functionality."""

def resolve_dns_records(domain, subdomains):
    """Resolve DNS records for domain and subdomains."""
    all_domains = [domain] + subdomains
    dns_data = {}
    
    for d in all_domains:
        dns_data[d] = {
            "A": resolve_a_record(d),
            "AAAA": resolve_aaaa_record(d),
            "CNAME": resolve_cname_record(d),
            "TXT": resolve_txt_record(d),
            "MX": resolve_mx_record(d)
        }
    
    return dns_data

import dns.resolver
import socket

def resolve_a_record(domain):
    """Resolve A record."""
    try:
        result = dns.resolver.resolve(domain, 'A')
        return [str(rdata) for rdata in result]
    except:
        return []

def resolve_aaaa_record(domain):
    """Resolve AAAA record."""
    try:
        result = dns.resolver.resolve(domain, 'AAAA')
        return [str(rdata) for rdata in result]
    except:
        return []

def resolve_cname_record(domain):
    """Resolve CNAME record."""
    try:
        result = dns.resolver.resolve(domain, 'CNAME')
        return str(result[0]) if result else None
    except:
        return None

def resolve_txt_record(domain):
    """Resolve TXT record."""
    try:
        result = dns.resolver.resolve(domain, 'TXT')
        return [str(rdata) for rdata in result]
    except:
        return []

def resolve_mx_record(domain):
    """Resolve MX record."""
    try:
        result = dns.resolver.resolve(domain, 'MX')
        return [str(rdata) for rdata in result]
    except:
        return []