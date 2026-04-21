import pytest
from src.utils import some_utility_function

def test_some_utility_function():
    input_data = "test input"
    expected_output = "expected output"
    assert some_utility_function(input_data) == expected_output

def test_another_utility_function():
    input_data = [1, 2, 3]
    expected_output = 6
    assert some_utility_function(input_data) == expected_output

# Add more tests as needed for other utility functions in utils.py