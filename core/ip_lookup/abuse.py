"""Abuse database checking for IP addresses."""

def check_abuse_databases(ip_address):
    """Check IP against abuse databases."""
    # Mock abuse database check
    # In real implementation, query AbuseIPDB, VirusTotal, etc.
    
    # Known bad IPs for demonstration
    known_bad_ips = ['192.168.1.100', '10.0.0.1']
    
    if ip_address in known_bad_ips:
        return {
            "abuse_reports": ["Reported for malicious activity"],
            "blacklisted": True
        }
    
    return {
        "abuse_reports": [],
        "blacklisted": False
    }