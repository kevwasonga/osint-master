"""Subdomain takeover detection functionality."""

from .signatures import get_takeover_signatures
from .checker import check_subdomain_vulnerability

def detect_takeover_risks(subdomains):
    """Detect potential subdomain takeover risks."""
    risks = []
    signatures = get_takeover_signatures()
    
    for subdomain in subdomains:
        vulnerability = check_subdomain_vulnerability(subdomain, signatures)
        if vulnerability:
            risks.append(vulnerability)
    
    return {
        "risks": risks,
        "total_subdomains": len(subdomains),
        "vulnerable_count": len(risks)
    }