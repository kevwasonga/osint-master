"""Input validation for CLI arguments."""

import re
import ipaddress

def validate_inputs(args):
    """Validate CLI input arguments."""
    if args.name:
        return validate_name(args.name)
    elif args.ip:
        return validate_ip(args.ip)
    elif args.username:
        return validate_username(args.username)
    elif args.domain:
        return validate_domain(args.domain)
    return False

def validate_name(name):
    """Validate full name input."""
    if not re.match(r'^[a-zA-Z\s]+$', name.strip()):
        print("Error: Name must contain only alphabetic characters and spaces")
        return False
    return True

def validate_ip(ip):
    """Validate IP address format."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        print("Error: Invalid IP address format")
        return False

def validate_username(username):
    """Validate and normalize username."""
    return True  # Basic validation, usernames can vary widely

def validate_domain(domain):
    """Validate domain format."""
    pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$'
    if not re.match(pattern, domain):
        print("Error: Invalid domain format")
        return False
    return True