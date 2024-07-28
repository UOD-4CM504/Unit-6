import pytest
from Dictionaries import add_from_list

def test_add_from_list_basic():
    test_dict = {"a": 1, "b": 2}
    items_to_add = [("e", 5), ("z", 26)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": 2, "e": 5, "z": 26}

def test_add_from_list_empty_dict():
    test_dict = {}
    items_to_add = [("x", 10), ("y", 20)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"x": 10, "y": 20}

def test_add_from_list_empty_list():
    test_dict = {"a": 1, "b": 2}
    items_to_add = []
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": 2}

def test_add_from_list_overwrite():
    test_dict = {"a": 1, "b": 2}
    items_to_add = [("b", 3), ("c", 4)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": 3, "c": 4}

def test_add_from_list_different_types():
    test_dict = {"a": 1, "b": "two"}
    items_to_add = [(3, "three"), (True, False)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": "two", 3: "three", True: False}

def test_add_from_list_large_input():
    test_dict = {str(i): i for i in range(1000)}
    items_to_add = [(str(i), i) for i in range(1000, 2000)]
    add_from_list(test_dict, items_to_add)
    assert len(test_dict) == 2000
    assert test_dict["1500"] == 1500

def test_add_from_list_no_side_effects():
    test_dict = {"a": 1, "b": 2}
    items_to_add = [("c", 3), ("d", 4)]
    original_items = items_to_add.copy()
    add_from_list(test_dict, items_to_add)
    assert items_to_add == original_items  # Ensure the input list is not modified