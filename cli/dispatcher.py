"""Command dispatcher for routing CLI commands to appropriate modules."""

from core.name_lookup.lookup import lookup_name
from core.ip_lookup.lookup import lookup_ip
from core.username_enum.enum import enumerate_username
from core.domain_enum.enum import enumerate_domain
from output.manager import save_results
from output.formatters import format_txt

def dispatch_command(args):
    """Dispatch command to appropriate module based on arguments."""
    result = None
    
    try:
        if args.name:
            print(f"Looking up name: {args.name}")
            result = lookup_name(args.name)
        elif args.ip:
            print(f"Analyzing IP: {args.ip}")
            result = lookup_ip(args.ip)
        elif args.username:
            print(f"Enumerating username: {args.username}")
            result = enumerate_username(args.username)
        elif args.domain:
            print(f"Enumerating domain: {args.domain}")
            result = enumerate_domain(args.domain)
        
        if result and args.output:
            save_results(result, args.output)
        elif result:
            print("\n" + format_txt(result))
            
    except Exception as e:
        print(f"Error: {e}")