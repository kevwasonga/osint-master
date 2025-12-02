"""Output formatting utilities."""

from datetime import datetime

def format_json(data):
    """Format data for JSON output."""
    return {
        "timestamp": datetime.now().isoformat(),
        "results": data
    }

def format_txt(data):
    """Format data for TXT output."""
    timestamp = datetime.now().isoformat()
    output = f"OSINT-Master Results - {timestamp}\n"
    output += "=" * 50 + "\n\n"
    
    # Format based on data type
    if "first_name" in data:
        output += format_name_data(data)
    elif "ip" in data:
        output += format_ip_data(data)
    elif "username" in data:
        output += format_username_data(data)
    elif "domain" in data:
        output += format_domain_data(data)
    else:
        output += str(data)
    
    return output

def format_name_data(data):
    """Format name lookup data."""
    output = f"First name: {data.get('first_name', 'N/A')}\n"
    output += f"Last name: {data.get('last_name', 'N/A')}\n"
    if data.get('phone'):
        output += f"Phone Number: {data['phone']}\n"
    if data.get('address'):
        output += f"Address: {data['address']}\n"
    if data.get('email'):
        output += f"Email: {data['email']}\n"
    
    social_media = data.get('social_media', {})
    if social_media:
        output += "Social Media:\n"
        for platform, url in social_media.items():
            if url:
                output += f"  {platform.title()}: {url}\n"
    
    return output

def format_ip_data(data):
    """Format IP lookup data."""
    output = f"IP: {data.get('ip', 'N/A')}\n"
    output += f"ISP: {data.get('isp', 'N/A')}\n"
    output += f"City: {data.get('city', 'N/A')}\n"
    output += f"Country: {data.get('country', 'N/A')}\n"
    if data.get('asn'):
        output += f"ASN: {data['asn']}\n"
    
    if data.get('blacklisted'):
        output += "Status: BLACKLISTED\n"
    else:
        output += "Status: Clean\n"
    
    abuse_reports = data.get('abuse_reports', [])
    if abuse_reports:
        output += "Abuse Reports:\n"
        for report in abuse_reports:
            output += f"  - {report}\n"
    
    return output

def format_username_data(data):
    """Format username enumeration data."""
    output = f"Username: {data.get('username', 'N/A')}\n"
    output += "Platform Results:\n"
    for platform, found in data.get('platforms', {}).items():
        status = "Found" if found else "Not Found"
        output += f"  {platform.title()}: {status}\n"
    return output

def format_domain_data(data):
    """Format domain enumeration data."""
    output = f"Main Domain: {data.get('domain', 'N/A')}\n\n"
    
    # WHOIS information
    whois_data = data.get('whois', {})
    if whois_data.get('registrar'):
        output += f"Registrar: {whois_data['registrar']}\n"
    
    # Subdomains
    subdomains = data.get('subdomains', [])
    output += f"Subdomains found: {len(subdomains)}\n"
    for subdomain in subdomains:
        output += f"  - {subdomain}\n"
    
    # Takeover risks
    takeover_risks = data.get('takeover_risks', {})
    risks = takeover_risks.get('risks', [])
    if risks:
        output += "\nPotential Subdomain Takeover Risks:\n"
        for risk in risks:
            output += f"  - Subdomain: {risk['subdomain']}\n"
            output += f"    CNAME: {risk['cname']}\n"
            output += f"    Risk Level: {risk['risk_level']}\n"
            output += f"    Recommendation: {risk['recommendation']}\n\n"
    
    return output