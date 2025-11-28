# 🔍 OSINT-Master

```
 ██████╗ ███████╗██╗███╗   ██╗████████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║   ██║███████╗██║██╔██╗ ██║   ██║       ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║   ██║╚════██║██║██║╚██╗██║   ██║       ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝███████║██║██║ ╚████║   ██║       ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

**Multi-function passive OSINT reconnaissance tool for cybersecurity learning and threat intelligence**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Security: Educational](https://img.shields.io/badge/security-educational-green.svg)](https://github.com/kevwasonga/osint-master)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Capabilities](#capabilities)
- [Ethical Guidelines](#ethical-guidelines)
- [Security Disclosure](#security-disclosure)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## 🎯 Overview

OSINT-Master is a comprehensive passive reconnaissance tool designed for cybersecurity professionals, researchers, and students. It performs ethical Open Source Intelligence (OSINT) gathering using publicly available data to identify potential security risks and vulnerabilities.

**Key Objectives:**
- 🔍 Passive information gathering from public sources
- 🛡️ Subdomain takeover risk detection
- 📊 Structured reporting and analysis
- 🎓 Educational cybersecurity tool
- ⚖️ Ethical and legal compliance

## ✨ Features

### Core Functionality
- **Name Lookup**: Extract personal information, phone numbers, addresses, and social media profiles
- **IP Analysis**: Geolocation, ISP details, and abuse database queries
- **Username Enumeration**: Check presence across 5+ social platforms
- **Domain Intelligence**: Subdomain discovery, DNS analysis, and SSL certificate inspection
- **Takeover Detection**: Identify potential subdomain takeover vulnerabilities

### Advanced Features
- 📄 Multiple output formats (JSON, TXT)
- 🔒 Secure API key management
- ⚡ Rate limiting and timeout handling
- 📝 Comprehensive logging and audit trails
- 🧪 Extensive test coverage

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Internet connection for API queries

### Quick Install

```bash
# Clone the repository
git clone https://github.com/kevwasonga/osint-master.git
cd osint-master

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make executable (optional)
chmod +x osintmaster/main.py
```

### Dependencies

```
requests>=2.31.0
dnspython>=2.4.2
beautifulsoup4>=4.12.2
python-whois>=0.8.0
shodan>=1.30.1
ipwhois>=1.2.0
click>=8.1.0
pytest>=7.4.0
```

## 💻 Usage

### Command Line Interface

```bash
python -m osintmaster --help
```

**Welcome to OSINT-Master multi-function Tool**

```
OPTIONS:
    -n  "Full Name"        Search information by full name
    -i  "IP Address"       Search information by IP address
    -u  "Username"         Search information by username
    -d  "Domain"           Enumerate subdomains and check for takeover risks
    -o  "FileName"         File name to save output
    --help                 Show this help message
```

### Basic Commands

```bash
# Name lookup
python -m osintmaster -n "John Doe" -o results.txt

# IP address analysis
python -m osintmaster -i "8.8.8.8" -o ip_analysis.json

# Username enumeration
python -m osintmaster -u "johndoe" -o username_check.txt

# Domain reconnaissance
python -m osintmaster -d "example.com" -o domain_report.json
```

## 📊 Examples

### Name Lookup Output
```bash
$ python -m osintmaster -n "John Doe" -o result1.txt
```
```
First name: John
Last name: Doe
Phone Number: +1234567890
Address: 123 Main St, City, Country
LinkedIn: linkedin.com/in/johndoe
Facebook: facebook.com/johndoe
Data Saved in result1.txt
```

### IP Address Analysis
```bash
$ python -m osintmaster -i "8.8.8.8" -o result2.txt
```
```
ISP: Google LLC
City: Mountain View
Country: United States
ASN: 15169
Known Issues: No reported abuse
Data Saved in result2.txt
```

### Username Enumeration
```bash
$ python -m osintmaster -u "johndoe" -o result3.txt
```
```
GitHub: Found
Twitter: Found
LinkedIn: Found
Instagram: Not Found
Reddit: Found
Recent Activity: Active on GitHub, last commit 2 days ago
Data Saved in result3.txt
```

### Domain & Subdomain Analysis
```bash
$ python -m osintmaster -d "example.com" -o result4.txt
```
```
Main Domain: example.com

Subdomains found: 3
  - www.example.com (IP: 93.184.216.34)
    SSL Certificate: Valid until 2025-03-01
  - mail.example.com (IP: 93.184.216.35)
    SSL Certificate: Valid until 2025-03-01
  - test.example.com (CNAME: abandoned-bucket.s3.amazonaws.com)
    SSL Certificate: Not found

Potential Subdomain Takeover Risks:
  - Subdomain: test.example.com
    CNAME record points to unclaimed AWS S3 bucket
    Recommended Action: Remove DNS record or claim resource

Data saved in result4.txt
```

### JSON Output Example
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "query_type": "domain",
  "target": "example.com",
  "results": {
    "main_domain": "example.com",
    "subdomains": [
      {
        "name": "www.example.com",
        "ip": "93.184.216.34",
        "ssl_valid": true,
        "ssl_expires": "2025-03-01"
      }
    ],
    "takeover_risks": [
      {
        "subdomain": "test.example.com",
        "risk_level": "high",
        "cname": "abandoned-bucket.s3.amazonaws.com",
        "recommendation": "Remove DNS record or claim resource"
      }
    ]
  }
}
```

## 🛠️ Capabilities

### Information Sources
- **Public APIs**: IP geolocation, Certificate Transparency logs
- **DNS Records**: A, AAAA, CNAME, TXT, MX records
- **WHOIS Data**: Domain registration information
- **Social Platforms**: GitHub, Twitter, LinkedIn, Instagram, Facebook, Reddit
- **SSL Certificates**: Certificate details and validation status

### Detection Capabilities
- **Subdomain Takeover Risks**: AWS S3, Azure, Netlify, Vercel, GitHub Pages
- **DNS Misconfigurations**: Dangling CNAME records
- **Historical Data**: Abuse databases and threat intelligence
- **Certificate Issues**: Expired or invalid SSL certificates

### Security Features
- 🔐 Secure API key storage via environment variables
- 🚫 Input sanitization and validation
- ⏱️ Request timeouts and rate limiting
- 📝 No credential storage in logs
- 🛡️ Passive reconnaissance only (no exploitation)

## ⚖️ Ethical Guidelines

### 🚨 IMPORTANT: Read Before Use

**This tool is for educational and authorized testing purposes ONLY.**

### Legal Requirements
- ✅ **Get Permission**: Always obtain explicit written permission before gathering information
- ✅ **Respect Privacy**: Collect only necessary data and store it securely
- ✅ **Follow Laws**: Adhere to GDPR, CFAA, and local privacy regulations
- ✅ **Educational Use**: Use solely for learning and improving security

### Prohibited Uses
- ❌ Unauthorized information gathering
- ❌ Stalking or harassment
- ❌ Identity theft or fraud
- ❌ Any illegal activities
- ❌ Exploitation of discovered vulnerabilities

### Best Practices
1. **Scope Limitation**: Only scan domains/systems you own or have permission to test
2. **Data Protection**: Securely handle and dispose of collected information
3. **Responsible Disclosure**: Report vulnerabilities through proper channels
4. **Documentation**: Maintain records of authorization and scope

## 🔒 Security Disclosure

If you discover potential subdomain takeover risks or other security vulnerabilities:

### For Your Own Domains
1. Immediately secure or remove vulnerable DNS records
2. Claim unclaimed resources if legitimate
3. Update DNS configurations

### For Third-Party Domains
1. **DO NOT** attempt to exploit the vulnerability
2. Contact the domain owner privately via:
   - Security contact from WHOIS data
   - security@domain.com email
   - Responsible disclosure platforms
3. Provide clear, non-threatening vulnerability details
4. Allow reasonable time for remediation

### Reporting Template
```
Subject: Security Vulnerability Report - Subdomain Takeover Risk

Dear Security Team,

I have identified a potential subdomain takeover vulnerability:

Domain: [subdomain.example.com]
Issue: CNAME points to unclaimed resource
Risk: Potential for malicious content hosting
Recommendation: Remove DNS record or claim resource

This report is made in good faith for security improvement.

Best regards,
[Your Name]
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/osint-master.git
cd osint-master

# Create development environment
python -m venv dev-env
source dev-env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```

### Contribution Process
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Write** tests for new functionality
4. **Ensure** all tests pass
5. **Follow** code style guidelines
6. **Commit** changes (`git commit -m 'Add amazing feature'`)
7. **Push** to branch (`git push origin feature/amazing-feature`)
8. **Open** a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints
- Write comprehensive tests
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 OSINT-Master Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## ⚠️ Disclaimer

**🚨 EDUCATIONAL PURPOSE ONLY 🚨**

This project is developed for **educational purposes** and **authorized security testing** only. The developers and contributors:

- ❌ **DO NOT** condone or support any illegal activities
- ❌ **ARE NOT** responsible for misuse of this tool
- ❌ **DO NOT** provide support for malicious use cases
- ✅ **ENCOURAGE** responsible and ethical use only

### Legal Notice
- Users are **solely responsible** for compliance with applicable laws
- **Unauthorized** use may violate local, state, and federal laws
- **Always obtain permission** before testing systems you do not own
- **Respect privacy** and data protection regulations

### Academic Use
This tool is designed for:
- 🎓 Cybersecurity education and training
- 🔬 Security research and analysis
- 🛡️ Authorized penetration testing
- 📚 Learning OSINT techniques and methodologies

**By using this tool, you acknowledge that you have read, understood, and agree to comply with all ethical and legal guidelines.**

---

**Made with ❤️ for the cybersecurity community**

For questions, issues, or contributions, please visit our [GitHub repository](https://github.com/kevwasonga/osint-master).