"""Integration tests for CLI functionality."""

import pytest
import subprocess
import sys
import os

def test_cli_help():
    """Test CLI help command."""
    result = subprocess.run([
        sys.executable, "-m", "cli.main", "--help"
    ], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    assert result.returncode == 0
    assert "OSINT-Master" in result.stdout

def test_cli_name_lookup():
    """Test CLI name lookup integration."""
    result = subprocess.run([
        sys.executable, "-m", "cli.main", "-n", "John Doe"
    ], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    assert "Welcome to OSINT-Master" in result.stdout