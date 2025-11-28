"""Test runner for all OSINT-Master tests."""

import pytest
import sys
import os

def run_all_tests():
    """Run all tests with coverage reporting."""
    test_args = [
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "tests/",  # Test directory
    ]
    
    return pytest.main(test_args)

def run_unit_tests():
    """Run only unit tests."""
    return pytest.main(["-v", "tests/unit/"])

def run_integration_tests():
    """Run only integration tests."""
    return pytest.main(["-v", "tests/integration/"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "unit":
            exit_code = run_unit_tests()
        elif sys.argv[1] == "integration":
            exit_code = run_integration_tests()
        else:
            print("Usage: python test_runner.py [unit|integration]")
            sys.exit(1)
    else:
        exit_code = run_all_tests()
    
    sys.exit(exit_code)