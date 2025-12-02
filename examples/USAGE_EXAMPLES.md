# OSINT-Master Usage Examples

## Quick Start

### 1. Domain Analysis with Takeover Detection
```bash
# Analyze a domain for subdomains and potential takeover risks
python -m cli.main -d "example.com" -o domain_analysis.txt

# JSON output for programmatic processing
python -m cli.main -d "example.com" -o domain_analysis.json
```

### 2. IP Address Investigation
```bash
# Analyze IP address for geolocation and abuse reports
python -m cli.main -i "8.8.8.8" -o ip_report.txt
```

### 3. Username Enumeration
```bash
# Check username presence across social platforms
python -m cli.main -u "johndoe" -o username_report.txt
```

### 4. Name Lookup
```bash
# Search for information associated with a name
python -m cli.main -n "John Doe" -o name_report.txt
```

## Subdomain Takeover Testing

### Demo Script
```bash
# Run the interactive demo to understand takeover detection
python tests/test_takeover_demo.py
```

### Real Domain Testing (Own Domains Only)
```bash
# Test your GitHub Pages domain
python -m cli.main -d "yourusername.github.io" -o github_scan.txt

# Test your company domain
python -m cli.main -d "yourcompany.com" -o company_scan.json
```

## Output Examples

### Domain Scan Output
```
Main Domain: example.com

Registrar: Example Registrar Inc.
Subdomains found: 5
  - www.example.com
  - mail.example.com
  - api.example.com
  - test.example.com
  - staging.example.com

Potential Subdomain Takeover Risks:
  - Subdomain: test.example.com
    CNAME: abandoned-bucket.s3.amazonaws.com
    Risk Level: high
    Recommendation: Remove DNS record or claim resource
```

### IP Analysis Output
```
IP: 8.8.8.8
ISP: Google LLC
City: Mountain View
Country: United States
ASN: 15169
Status: Clean
```

### Username Check Output
```
Username: johndoe
Platform Results:
  Github: Found
  Twitter: Found
  Linkedin: Found
  Instagram: Not Found
  Reddit: Found
  Facebook: Found
```

## Automation Examples

### Bash Script for Regular Monitoring
```bash
#!/bin/bash
# monitor_domain.sh

DOMAIN="yourdomain.com"
DATE=$(date +%Y%m%d)
OUTPUT_FILE="scan_${DOMAIN}_${DATE}.json"

echo "Scanning $DOMAIN for subdomain takeover risks..."
python -m cli.main -d "$DOMAIN" -o "$OUTPUT_FILE"

# Check for vulnerabilities
if grep -q "Potential Subdomain Takeover Risks" "$OUTPUT_FILE"; then
    echo "WARNING: Vulnerabilities detected in $OUTPUT_FILE"
    # Add notification logic here (email, Slack, etc.)
else
    echo "No vulnerabilities detected"
fi
```

### Python Integration
```python
#!/usr/bin/env python3
import subprocess
import json
import sys

def scan_domain(domain):
    """Scan domain and return results."""
    output_file = f"{domain}_scan.json"
    
    # Run OSINT-Master
    result = subprocess.run([
        sys.executable, "-m", "cli.main",
        "-d", domain,
        "-o", output_file
    ], capture_output=True, text=True)
    
    # Load results
    with open(output_file, 'r') as f:
        return json.load(f)

# Usage
if __name__ == "__main__":
    domain = "example.com"
    results = scan_domain(domain)
    
    # Process results
    takeover_risks = results.get('results', {}).get('takeover_risks', {})
    if takeover_risks.get('risks'):
        print(f"Found {len(takeover_risks['risks'])} potential takeover risks!")
        for risk in takeover_risks['risks']:
            print(f"- {risk['subdomain']}: {risk['recommendation']}")
    else:
        print("No takeover risks detected")
```

## Best Practices

### 1. Ethical Testing
- Only test domains you own or have explicit permission to test
- Document your authorization and testing scope
- Use for educational and security improvement purposes only

### 2. Regular Monitoring
- Set up automated scans for your domains
- Monitor Certificate Transparency logs
- Implement DNS change alerts

### 3. Incident Response
- Have a plan for addressing discovered vulnerabilities
- Know how to quickly remove or update DNS records
- Establish communication channels for security alerts

### 4. Documentation
- Keep records of all scans and findings
- Document remediation actions taken
- Maintain an inventory of all subdomains and services

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Install missing dependencies
pip install -r requirements.txt
```

#### Timeout Errors
```bash
# Increase timeout in config/settings.py
API_TIMEOUT = 30  # Increase from default 10 seconds
```

#### Permission Errors
```bash
# Ensure you have write permissions for output directory
chmod 755 output/
```

### Getting Help
- Check the README.md for detailed documentation
- Review the test files for usage examples
- Ensure all dependencies are properly installed