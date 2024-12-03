
import pytest
from unittest.mock import mock_open, patch
from day1.src.day1 import calculate_total_distance

# Assuming the function to be tested is in a module called 'day1'
# from day1 import calculate_total_distance, read_and_split_columns

def test_calculate_total_distance_example_case():
    # Mock data (example from the problem statement)
    mock_data = "3 4\n4 3\n2 5\n1 3\n3 9\n3 3\n"
    
    # Patch the open function in the module where the file is being read
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = calculate_total_distance()
    
    # The expected result from the example
    expected_result = 11
    
    # Assert the result is as expected
    assert result == expected_result