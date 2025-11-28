"""Unit tests for name lookup functionality."""

import pytest
from core.name_lookup.parser import parse_name
from core.name_lookup.lookup import lookup_name

def test_parse_name_full():
    """Test parsing full name."""
    result = parse_name("John Michael Doe")
    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"
    assert result["middle_name"] == "Michael"

def test_parse_name_two_parts():
    """Test parsing two-part name."""
    result = parse_name("John Doe")
    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"
    assert result["middle_name"] == ""

def test_parse_name_single():
    """Test parsing single name."""
    result = parse_name("John")
    assert result["first_name"] == "John"
    assert result["last_name"] == ""
    assert result["middle_name"] == ""

def test_lookup_name_structure():
    """Test name lookup returns correct structure."""
    result = lookup_name("John Doe")
    assert "first_name" in result
    assert "last_name" in result