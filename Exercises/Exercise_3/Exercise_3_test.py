import pytest
from unittest.mock import patch
import io
from Exercise_3 import main


@pytest.mark.parametrize("inputs, expected_output", [
    (["1", "5", "6", "10", "q"], "The reverse of the numbers entered is:\n10\n6\n5\n1\n"),
    (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
     "The reverse of the numbers entered is:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"),
    (["q"], "No numbers entered.\n"),
    (["1", "2", "q"], "The reverse of the numbers entered is:\n2\n1\n"),
    (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
     "The reverse of the numbers entered is:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"),
])
def test_main(inputs, expected_output):
    with patch('builtins.input', side_effect=inputs), \
            patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

    assert output.strip() == expected_output.strip()


if __name__ == "__main__":
    pytest.main([__file__])