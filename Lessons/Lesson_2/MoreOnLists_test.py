import pytest
from MoreOnLists import change_list


def test_change_list():
    # Test case 1
    test_list = ["Pear", "Orange", "Peach", "Apple"]
    assert change_list(test_list) == ["Apple", "Banana", "Peach", "Pear"]

    # Test case 2
    test_list = ["Sam", "Bradley", "Wayne"]
    assert change_list(test_list) == ['Banana', 'Sam', 'Wayne']


def test_original_list_unchanged():
    # Test that the original list is not modified
    test_list = ["Pear", "Orange", "Peach", "Apple"]
    original_list = test_list.copy()
    change_list(test_list)
    assert test_list == original_list

    test_list = ["Sam", "Bradley", "Wayne"]
    original_list = test_list.copy()
    change_list(test_list)
    assert test_list == original_list