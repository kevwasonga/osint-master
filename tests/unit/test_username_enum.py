"""Unit tests for username enumeration."""

import pytest
from core.username_enum.enum import enumerate_username

def test_username_normalization():
    """Test username normalization."""
    result = enumerate_username("@testuser")
    assert result["username"] == "testuser"
    
    result = enumerate_username("testuser")
    assert result["username"] == "testuser"

def test_enumerate_username_structure():
    """Test username enumeration structure."""
    result = enumerate_username("testuser")
    assert "username" in result
    assert "platforms" in result
    assert "metadata" in result