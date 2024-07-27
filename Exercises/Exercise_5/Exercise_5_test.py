import pytest
from io import StringIO
from unittest.mock import patch
from Exercise_5 import look_up, add, edit, delete, list_all


@pytest.fixture
def sample_address_book():
    return {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }


def test_look_up(sample_address_book):
    assert look_up(sample_address_book, "Sam") == "MS308, Markeaton St, Derby"
    assert look_up(sample_address_book, "Sherlock") == "221B Baker Street, London"


def test_add(sample_address_book):
    add(sample_address_book, "John", "742 Evergreen Terrace, Springfield")
    assert "John" in sample_address_book
    assert sample_address_book["John"] == "742 Evergreen Terrace, Springfield"


def test_edit(sample_address_book):
    edit(sample_address_book, "Sam", "New Address, New City")
    assert sample_address_book["Sam"] == "New Address, New City"


def test_delete(sample_address_book):
    delete(sample_address_book, "Sherlock")
    assert "Sherlock" not in sample_address_book


def test_list_all(sample_address_book):
    expected_output = (
        "Name: Sam\n"
        "Address: MS308, Markeaton St, Derby\n"
        "\n"
        "Name: Sherlock\n"
        "Address: 221B Baker Street, London\n"
        "\n"
    )

    with patch('sys.stdout', new=StringIO()) as fake_out:
        list_all(sample_address_book)
        assert fake_out.getvalue() == expected_output


def test_look_up_nonexistent(sample_address_book):
    with pytest.raises(KeyError):
        look_up(sample_address_book, "Nonexistent")


def test_edit_nonexistent(sample_address_book):
    original_length = len(sample_address_book)
    non_existent_name = "Nonexistent"
    new_address = "Some Address"

    # Try to edit a non-existent entry
    edit(sample_address_book, non_existent_name, new_address)

    # Check if the address book length has changed
    if len(sample_address_book) == original_length:
        # If length hasn't changed, the entry wasn't added
        assert non_existent_name not in sample_address_book
    else:
        # If length has changed, the entry was added (which is also acceptable behavior)
        assert sample_address_book[non_existent_name] == new_address


def test_delete_nonexistent(sample_address_book):
    with pytest.raises(KeyError):
        delete(sample_address_book, "Nonexistent")