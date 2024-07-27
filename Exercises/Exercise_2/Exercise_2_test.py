import pytest
from unittest.mock import patch
import io
import re
from Exercise_2 import main, advanced_main, rand_num_list_gen

def test_rand_num_list_gen():
    # Test with default parameters
    result = rand_num_list_gen()
    assert len(result) == 100
    assert all(1 <= num <= 50 for num in result)

    # Test with custom parameters
    result = rand_num_list_gen(num=50, lower=10, upper=20)
    assert len(result) == 50
    assert all(10 <= num <= 20 for num in result)

def test_main():
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

    # Check if all ranges are present
    ranges = ["1..10", "11..20", "21..30", "31..40", "41..50"]
    for range_str in ranges:
        assert range_str in output

    # Check if the sum of all counts is 100
    counts = [int(line.split(": ")[1]) for line in output.split("\n") if ".." in line]
    assert sum(counts) == 100

@pytest.mark.parametrize("num_input,ranges_input", [
    ("100", "1..20,21..30,31..45,46..50"),
    ("200", "1..30,1..50")
])
def test_advanced_main(num_input, ranges_input):
    with patch('builtins.input', side_effect=[num_input, ranges_input]), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        advanced_main()
        output = fake_out.getvalue()

    # Check if all input ranges are present in the output
    for range_str in ranges_input.split(','):
        assert range_str in output

    # Extract counts and check if their sum matches the input number
    counts = [int(re.search(r': (\d+)', line).group(1)) for line in output.split('\n') if '..' in line]
    assert sum(counts) >= int(num_input)  # Sum should be >= input number due to possible overlapping ranges

if __name__ == "__main__":
    pytest.main([__file__])