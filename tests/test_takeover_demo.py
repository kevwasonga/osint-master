#!/usr/bin/env python3
"""Demo script to test subdomain takeover detection."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.takeover_detector.detector import detect_takeover_risks
from core.takeover_detector.signatures import get_takeover_signatures
from core.takeover_detector.checker import check_subdomain_vulnerability

def test_takeover_signatures():
    """Test takeover signatures are loaded correctly."""
    print("=== Testing Takeover Signatures ===")
    signatures = get_takeover_signatures()
    
    print(f"Loaded {len(signatures)} provider signatures:")
    for provider, sig in signatures.items():
        print(f"  - {provider}: {len(sig['cname_patterns'])} patterns, {len(sig['error_messages'])} error messages")
    
    return signatures

def test_mock_vulnerable_subdomains():
    """Test with mock vulnerable subdomains."""
    print("\n=== Testing Mock Vulnerable Subdomains ===")
    
    # Mock subdomains that would be vulnerable
    mock_subdomains = [
        "test.example.com",
        "staging.example.com", 
        "old.example.com"
    ]
    
    # Mock CNAME records that point to potentially vulnerable services
    mock_cnames = {
        "test.example.com": "abandoned-bucket.s3.amazonaws.com",
        "staging.example.com": "old-site.netlify.com",
        "old.example.com": "deleted-app.azurewebsites.net"
    }
    
    print("Mock subdomains to test:")
    for subdomain in mock_subdomains:
        cname = mock_cnames.get(subdomain, "No CNAME")
        print(f"  - {subdomain} -> {cname}")
    
    # Test detection
    result = detect_takeover_risks(mock_subdomains)
    
    print(f"\nDetection Results:")
    print(f"  Total subdomains: {result['total_subdomains']}")
    print(f"  Vulnerable count: {result['vulnerable_count']}")
    print(f"  Risks found: {len(result['risks'])}")
    
    return result

def test_real_subdomain_example():
    """Test with a real example (educational purposes only)."""
    print("\n=== Testing Real Subdomain Example ===")
    
    # Example of how to test a real domain (use only domains you own!)
    test_domain = "example.com"  # Safe test domain
    
    print(f"Testing domain: {test_domain}")
    print("Note: This is for educational demonstration only!")
    print("Always get permission before testing real domains.")
    
    # Mock some common subdomains
    common_subs = [f"www.{test_domain}", f"mail.{test_domain}", f"ftp.{test_domain}"]
    
    result = detect_takeover_risks(common_subs)
    print(f"Results: {result['vulnerable_count']} potential risks found")
    
    return result

def demonstrate_detection_process():
    """Demonstrate the step-by-step detection process."""
    print("\n=== Demonstrating Detection Process ===")
    
    signatures = get_takeover_signatures()
    test_subdomain = "abandoned.example.com"
    test_cname = "old-bucket.s3.amazonaws.com"
    
    print(f"1. Checking subdomain: {test_subdomain}")
    print(f"2. CNAME points to: {test_cname}")
    
    # Check against each provider
    for provider, sig in signatures.items():
        print(f"\n3. Checking against {provider}:")
        print(f"   Patterns: {sig['cname_patterns']}")
        
        # Check if CNAME matches any pattern
        matches = [pattern for pattern in sig['cname_patterns'] if pattern in test_cname]
        if matches:
            print(f"   MATCH: {matches[0]} found in CNAME")
            print(f"   -> Potential {provider} takeover risk!")
            break
        else:
            print(f"   No match for {provider}")

def show_mitigation_strategies():
    """Show mitigation strategies for subdomain takeover."""
    print("\n=== Subdomain Takeover Mitigation Strategies ===")
    
    strategies = {
        "Prevention": [
            "Maintain an inventory of all subdomains",
            "Remove DNS records when services are decommissioned",
            "Use automation to monitor DNS changes",
            "Implement DNS hygiene policies"
        ],
        "Detection": [
            "Regular subdomain enumeration scans",
            "Monitor Certificate Transparency logs",
            "Check for dangling CNAME records",
            "Automated takeover detection tools"
        ],
        "Response": [
            "Immediately remove vulnerable DNS records",
            "Claim the abandoned resource if legitimate",
            "Update DNS to point to active services",
            "Document and track remediation"
        ]
    }
    
    for category, items in strategies.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item}")

def main():
    """Run all takeover detection tests."""
    print("OSINT-Master Subdomain Takeover Detection Demo")
    print("=" * 60)
    
    try:
        # Test signatures
        signatures = test_takeover_signatures()
        
        # Test mock vulnerabilities
        mock_results = test_mock_vulnerable_subdomains()
        
        # Test real example
        real_results = test_real_subdomain_example()
        
        # Demonstrate process
        demonstrate_detection_process()
        
        # Show mitigation
        show_mitigation_strategies()
        
        print("\n" + "=" * 60)
        print("Subdomain takeover detection demo completed!")
        print("\nIMPORTANT REMINDERS:")
        print("   - Only test domains you own or have permission to test")
        print("   - This tool is for educational and authorized testing only")
        print("   - Report vulnerabilities responsibly through proper channels")
        
    except Exception as e:
        print(f"Error during testing: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())