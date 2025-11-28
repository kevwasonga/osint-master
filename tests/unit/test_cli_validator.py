"""Unit tests for CLI input validation."""

import pytest
from cli.validator import validate_name, validate_ip, validate_username, validate_domain

def test_validate_name():
    """Test name validation."""
    assert validate_name("John Doe") == True
    assert validate_name("John123") == False
    assert validate_name("") == False

def test_validate_ip():
    """Test IP address validation."""
    assert validate_ip("8.8.8.8") == True
    assert validate_ip("2001:db8::1") == True
    assert validate_ip("invalid") == False

def test_validate_username():
    """Test username validation."""
    assert validate_username("testuser") == True
    assert validate_username("@testuser") == True

def test_validate_domain():
    """Test domain validation."""
    assert validate_domain("example.com") == True
    assert validate_domain("sub.example.com") == True
    assert validate_domain("invalid..domain") == False