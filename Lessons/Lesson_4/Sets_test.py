import pytest
from Sets import items_in_both

def test_items_in_both_basic():
    a = {1, 2, 3}
    b = {1, 4, 5, 6}
    assert items_in_both(a, b) == {1}

def test_items_in_both_no_common():
    a = {1, 2, 3}
    b = {4, 5, 6}
    assert items_in_both(a, b) == set()

def test_items_in_both_all_common():
    a = {1, 2, 3}
    b = {1, 2, 3}
    assert items_in_both(a, b) == {1, 2, 3}

def test_items_in_both_multiple_common():
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    assert items_in_both(a, b) == {3, 4, 5}

def test_items_in_both_empty_set():
    a = set()
    b = {1, 2, 3}
    assert items_in_both(a, b) == set()

def test_items_in_both_different_types():
    a = {1, 'a', True}
    b = {1, 'b', False, 'a'}
    assert items_in_both(a, b) == {1, 'a'}

def test_items_in_both_large_sets():
    a = set(range(1, 1001))  # {1, 2, ..., 1000}
    b = set(range(500, 1501))  # {500, 501, ..., 1500}
    expected = set(range(500, 1001))
    assert items_in_both(a, b) == expected