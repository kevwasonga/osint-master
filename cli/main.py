#!/usr/bin/env python3
"""Main CLI entry point for OSINT-Master."""

from .parser import create_parser
from .validator import validate_inputs
from .dispatcher import dispatch_command

def main():
    """Main CLI function."""
    print("Welcome to OSINT-Master multi-function Tool")
    
    parser = create_parser()
    args = parser.parse_args()
    
    if not any([args.name, args.ip, args.username, args.domain]):
        parser.print_help()
        return
    
    # Validate inputs
    if not validate_inputs(args):
        return
    
    # Dispatch to appropriate module
    dispatch_command(args)

if __name__ == "__main__":
    main()