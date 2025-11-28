#!/usr/bin/env python3
"""CLI argument parser for OSINT-Master."""

import argparse

def create_parser():
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="OSINT-Master multi-function Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m osintmaster -n "John Doe" -o results.txt
  python -m osintmaster -i "8.8.8.8" -o ip_analysis.json
  python -m osintmaster -u "username" -o user_check.txt
  python -m osintmaster -d "example.com" -o domain_report.json
        """
    )
    
    parser.add_argument("-n", "--name", help="Search information by full name")
    parser.add_argument("-i", "--ip", help="Search information by IP address") 
    parser.add_argument("-u", "--username", help="Search information by username")
    parser.add_argument("-d", "--domain", help="Enumerate subdomains and check for takeover risks")
    parser.add_argument("-o", "--output", help="File name to save output")
    
    return parser