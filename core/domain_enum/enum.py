"""Domain enumeration functionality."""

from .whois import get_whois_data
from .subdomains import discover_subdomains
from .dns import resolve_dns_records
from .ssl import check_ssl_certificates
from core.takeover_detector.detector import detect_takeover_risks

def enumerate_domain(domain):
    """Main domain enumeration function."""
    whois_data = get_whois_data(domain)
    subdomains = discover_subdomains(domain)
    dns_records = resolve_dns_records(domain, subdomains)
    ssl_info = check_ssl_certificates(subdomains)
    takeover_risks = detect_takeover_risks(subdomains)
    
    return {
        "domain": domain,
        "whois": whois_data,
        "subdomains": subdomains,
        "dns_records": dns_records,
        "ssl_info": ssl_info,
        "takeover_risks": takeover_risks
    }