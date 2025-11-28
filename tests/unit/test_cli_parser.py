"""Unit tests for CLI parser functionality."""

import pytest
from cli.parser import create_parser

def test_parser_creation():
    """Test parser creation."""
    parser = create_parser()
    assert parser is not None

def test_parser_arguments():
    """Test parser accepts all required arguments."""
    parser = create_parser()
    args = parser.parse_args(["-n", "John Doe", "-o", "test.txt"])
    assert args.name == "John Doe"
    assert args.output == "test.txt"

def test_parser_help():
    """Test parser help functionality."""
    parser = create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])