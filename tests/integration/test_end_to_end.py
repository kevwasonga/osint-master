"""End-to-end integration tests."""

import pytest
import tempfile
import os
from cli.main import main
from unittest.mock import patch

def test_end_to_end_name_lookup():
    """Test complete name lookup workflow."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name
    
    try:
        with patch('sys.argv', ['main.py', '-n', 'John Doe', '-o', temp_file]):
            main()
        
        assert os.path.exists(temp_file)
        with open(temp_file, 'r') as f:
            content = f.read()
            assert "OSINT-Master Results" in content
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)