"""Unit tests for subdomain takeover detection."""

import pytest
from core.takeover_detector.detector import detect_takeover_risks
from core.takeover_detector.signatures import get_takeover_signatures

def test_detect_takeover_structure():
    """Test takeover detection structure."""
    result = detect_takeover_risks([])
    assert "risks" in result
    assert "total_subdomains" in result
    assert "vulnerable_count" in result
    assert result["total_subdomains"] == 0

def test_get_takeover_signatures():
    """Test takeover signatures."""
    signatures = get_takeover_signatures()
    assert "aws_s3" in signatures
    assert "azure" in signatures
    assert "netlify" in signatures