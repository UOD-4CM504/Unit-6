import pytest
from Exercise_1 import find_max_row

@pytest.mark.parametrize("grid, expected_output", [
    ([[1, 2, 3], [4, 2, 1], [4, 5, 4]], 3),
    ([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 1),
    ([[1, 2, 3], [3], [2, 1, 3, 4]], 3),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
    ([[10], [5, 5], [3, 3, 3], [2, 2, 2, 2]], 1),
    ([[-1, -2, -3], [-4, -5, -6]], 1),
    ([[0]], 1),
    ([[1, 2], [2, 1], [1, 1, 1]], 1),
])
def test_find_max_row(grid, expected_output):
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"

if __name__ == "__main__":
    pytest.main([__file__])