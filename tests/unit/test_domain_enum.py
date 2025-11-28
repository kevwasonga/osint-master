"""Unit tests for domain enumeration."""

import pytest
from core.domain_enum.enum import enumerate_domain

def test_enumerate_domain_structure():
    """Test domain enumeration structure."""
    result = enumerate_domain("example.com")
    assert "domain" in result
    assert "subdomains" in result
    assert "whois" in result
    assert "dns_records" in result
    assert result["domain"] == "example.com"