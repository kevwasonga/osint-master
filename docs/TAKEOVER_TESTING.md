# Subdomain Takeover Testing Guide

## Overview

Subdomain takeover occurs when a subdomain points to a service (via CNAME) that has been decommissioned or is unclaimed, allowing attackers to claim the service and serve malicious content.

## How to Test Subdomain Takeover Detection

### 1. Understanding the Process

```
Domain: sub.example.com
CNAME: old-bucket.s3.amazonaws.com
Status: Bucket doesn't exist → VULNERABLE
```

### 2. Safe Testing Methods

#### A. Use Test Domains
```bash
# Test with safe domains
python tests/test_takeover_demo.py
```

#### B. Test Your Own Domains
```bash
# Only test domains you own
python -m cli.main -d "yourdomain.com" -o results.txt
```

#### C. Mock Testing
```python
# Create mock scenarios
mock_subdomains = [
    "test.example.com",      # Points to abandoned S3 bucket
    "staging.example.com",   # Points to deleted Netlify site
    "old.example.com"        # Points to removed Azure app
]
```

### 3. Detection Signatures

The tool checks for these vulnerable patterns:

#### AWS S3
- **CNAME patterns**: `.s3.amazonaws.com`, `.s3-website`
- **Error messages**: "NoSuchBucket", "The specified bucket does not exist"

#### Azure
- **CNAME patterns**: `.azurewebsites.net`, `.cloudapp.net`
- **Error messages**: "404", "Web app does not exist"

#### Netlify
- **CNAME patterns**: `.netlify.com`, `.netlify.app`
- **Error messages**: "Not Found", "Site not found"

#### Vercel
- **CNAME patterns**: `.vercel.app`, `.now.sh`
- **Error messages**: "404", "The deployment could not be found"

#### GitHub Pages
- **CNAME patterns**: `.github.io`
- **Error messages**: "404", "There isn't a GitHub Pages site here"

### 4. Testing Commands

#### Basic Domain Scan
```bash
python -m cli.main -d "example.com" -o domain_scan.txt
```

#### JSON Output for Analysis
```bash
python -m cli.main -d "example.com" -o domain_scan.json
```

#### Run Demo Script
```bash
python tests/test_takeover_demo.py
```

### 5. Expected Output

#### Vulnerable Subdomain Found
```
Potential Subdomain Takeover Risks:
  - Subdomain: test.example.com
    CNAME record points to unclaimed AWS S3 bucket
    Recommended Action: Remove DNS record or claim resource
```

#### Clean Domain
```
Main Domain: example.com
Subdomains found: 3
  - www.example.com (IP: 1.2.3.4)
  - mail.example.com (IP: 1.2.3.5)
  - api.example.com (IP: 1.2.3.6)

No subdomain takeover risks detected.
```

### 6. Manual Verification

#### Check CNAME Record
```bash
dig CNAME suspicious.example.com
```

#### Test HTTP Response
```bash
curl -I http://suspicious.example.com
```

#### Verify Service Status
- Visit the CNAME target directly
- Look for error messages indicating unclaimed resources

### 7. Common Vulnerable Scenarios

#### Scenario 1: Abandoned S3 Bucket
```
subdomain.example.com → old-bucket.s3.amazonaws.com
HTTP Response: "NoSuchBucket"
Risk: High - Bucket can be claimed
```

#### Scenario 2: Deleted Netlify Site
```
app.example.com → deleted-site.netlify.com
HTTP Response: "Site not found"
Risk: High - Site name can be reclaimed
```

#### Scenario 3: Removed Azure App
```
api.example.com → removed-app.azurewebsites.net
HTTP Response: "Web app does not exist"
Risk: Medium - App name might be reclaimable
```

### 8. Ethical Testing Guidelines

#### ✅ DO
- Test only domains you own or have explicit permission to test
- Use the tool for educational purposes
- Report vulnerabilities responsibly
- Document your testing scope and authorization

#### ❌ DON'T
- Test third-party domains without permission
- Attempt to exploit discovered vulnerabilities
- Claim abandoned resources belonging to others
- Use findings for malicious purposes

### 9. Remediation Steps

#### If Vulnerability Found
1. **Immediate**: Remove the vulnerable DNS record
2. **Alternative**: Point DNS to an active, controlled resource
3. **Long-term**: Implement DNS hygiene policies
4. **Monitor**: Set up alerts for DNS changes

#### Prevention
- Maintain subdomain inventory
- Automate DNS cleanup when services are decommissioned
- Regular subdomain takeover scans
- DNS change approval processes

### 10. Integration with CI/CD

#### GitHub Actions Example
```yaml
name: Subdomain Takeover Check
on: [push, pull_request]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Takeover Detection
        run: python -m cli.main -d "${{ secrets.DOMAIN }}" -o scan_results.json
```

### 11. Reporting Template

```
Subject: Subdomain Takeover Vulnerability Report

Domain: [affected-subdomain.example.com]
CNAME Target: [abandoned-service.provider.com]
Provider: [AWS S3/Netlify/Azure/etc.]
Risk Level: [High/Medium/Low]
Evidence: [HTTP response/error message]

Recommendation:
- Remove DNS record immediately
- Or point to active, controlled resource

This report is made in good faith for security improvement.
```

## Conclusion

Subdomain takeover detection is a critical security practice. Always test responsibly and ethically, focusing on domains you own or have permission to test. Use the findings to improve your organization's DNS hygiene and security posture.