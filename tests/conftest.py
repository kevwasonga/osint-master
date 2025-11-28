"""Pytest configuration and fixtures."""

import pytest
import tempfile
import os

@pytest.fixture
def temp_output_file():
    """Create temporary output file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name
    
    yield temp_file
    
    # Cleanup
    if os.path.exists(temp_file):
        os.unlink(temp_file)

@pytest.fixture
def sample_data():
    """Sample data for testing."""
    return {
        "name": "John Doe",
        "ip": "8.8.8.8",
        "username": "testuser",
        "domain": "example.com"
    }