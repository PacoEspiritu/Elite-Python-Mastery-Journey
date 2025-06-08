# test_qa_functions.py - Your first pytest adventure!

import pytest

def calculate_success_rate(passed, total):
    """Calculate success rate as percentage"""
    return (passed / total) * 100

def calculate_total_tests(passed, failed):
    """Calculate total tests from passed and failed"""
    return passed + failed

# ============================================================================
# YOUR FIRST TESTS!
# ============================================================================

def test_chrome_success_rate():
    # Test Chrome: 8 passed out of 10 total = 80%
    result = calculate_success_rate(8, 10)
    assert result == 80.0

def test_safari_success_rate():
    # Test Safari: 9 passed out of 10 total = 90%
    result = calculate_success_rate(9, 10)
    assert result == 90.0

def test_total_calculation():
    # Test total calculation: 8 passed + 2 failed = 10 total
    result = calculate_total_tests(8, 2)
    assert result == 10