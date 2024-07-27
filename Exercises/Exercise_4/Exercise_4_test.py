import pytest
from unittest.mock import patch
import io
import re
from Exercise_4 import main


def run_test(input_values, expected_coin_output):
    input_mock = iter(input_values)
    output = io.StringIO()

    def mock_input(prompt):
        return next(input_mock)

    with patch('builtins.input', mock_input):
        with patch('sys.stdout', output):
            main()

    actual_output = output.getvalue()

    # Extract numbers from the output
    numbers = re.findall(r'\d+', actual_output)

    # Group numbers into pairs (coin denomination and count)
    actual_coin_output = list(zip(numbers[::2], numbers[1::2]))

    assert actual_coin_output == expected_coin_output, f"Expected {expected_coin_output}, but got {actual_coin_output}"


def test_correct_change():
    input_values = ["100", "42"]
    expected_coin_output = [
        ('50', '1'), ('20', '0'), ('10', '0'),
        ('5', '1'), ('2', '1'), ('1', '1')
    ]
    run_test(input_values, expected_coin_output)


def test_correct_change_different_amounts():
    input_values = ["66", "33"]
    expected_coin_output = [
        ('50', '0'), ('20', '1'), ('10', '1'),
        ('5', '0'), ('2', '1'), ('1', '1')
    ]
    run_test(input_values, expected_coin_output)


def test_item_costs_more():
    input_values = ["75", "80"]
    expected_coin_output = []  # No coins should be output
    run_test(input_values, expected_coin_output)


def test_invalid_amount_over_100():
    input_values = ["105"]
    expected_coin_output = []  # No coins should be output
    run_test(input_values, expected_coin_output)


def test_invalid_amount_negative():
    input_values = ["-10"]
    expected_coin_output = []  # No coins should be output
    run_test(input_values, expected_coin_output)


def test_exact_amount():
    input_values = ["50", "50"]
    expected_coin_output = [
        ('50', '0'), ('20', '0'), ('10', '0'),
        ('5', '0'), ('2', '0'), ('1', '0')
    ]
    run_test(input_values, expected_coin_output)