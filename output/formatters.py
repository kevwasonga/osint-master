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
    return output

def format_ip_data(data):
    """Format IP lookup data."""
    output = f"IP: {data.get('ip', 'N/A')}\n"
    output += f"ISP: {data.get('isp', 'N/A')}\n"
    output += f"City: {data.get('city', 'N/A')}\n"
    output += f"Country: {data.get('country', 'N/A')}\n"
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
    output = f"Domain: {data.get('domain', 'N/A')}\n"
    subdomains = data.get('subdomains', [])
    output += f"Subdomains found: {len(subdomains)}\n"
    for subdomain in subdomains:
        output += f"  - {subdomain}\n"
    return output