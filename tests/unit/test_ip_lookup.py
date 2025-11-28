"""Unit tests for IP lookup functionality."""

import pytest
from core.ip_lookup.lookup import lookup_ip

def test_lookup_ip_structure():
    """Test IP lookup returns correct structure."""
    result = lookup_ip("8.8.8.8")
    assert "ip" in result
    assert "isp" in result
    assert "city" in result
    assert "country" in result
    assert result["ip"] == "8.8.8.8"

def test_lookup_ip_ipv6():
    """Test IPv6 lookup."""
    result = lookup_ip("2001:db8::1")
    assert result["ip"] == "2001:db8::1"