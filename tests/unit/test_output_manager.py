"""Unit tests for output management."""

import pytest
import os
import json
from output.manager import save_results
from output.formatters import format_json, format_txt

def test_format_json():
    """Test JSON formatting."""
    data = {"test": "data"}
    result = format_json(data)
    assert "timestamp" in result
    assert "results" in result
    assert result["results"] == data

def test_format_txt():
    """Test TXT formatting."""
    data = {"test": "data"}
    result = format_txt(data)
    assert "OSINT-Master Results" in result
    assert "=" in result

def test_save_results_json(tmp_path):
    """Test saving JSON results."""
    data = {"test": "data"}
    filename = tmp_path / "test.json"
    save_results(data, str(filename))
    assert filename.exists()
    
    with open(filename) as f:
        saved_data = json.load(f)
    assert "results" in saved_data