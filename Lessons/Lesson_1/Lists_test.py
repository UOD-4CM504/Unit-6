import pytest
from Lists import longest_word, num_characters

@pytest.fixture
def sample_string_list():
    return [
        ["Hello", "World"],
        ["You", "say", "you", "want", "a", "revolution"],
        ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]
    ]

@pytest.fixture
def sample_string_list2():
    return [["Hello", "World"], ["Apple", "Pears"]]

def test_longest_word(sample_string_list, sample_string_list2):
    assert longest_word(sample_string_list) == "revolution"
    assert longest_word(sample_string_list2) == "Hello"

def test_num_characters(sample_string_list, sample_string_list2):
    assert num_characters(sample_string_list) == 105
    assert num_characters(sample_string_list2) == 20

def test_longest_word_empty_list():
    assert longest_word([]) is None

def test_num_characters_empty_list():
    assert num_characters([]) == 0

def test_longest_word_multiple_longest():
    test_list = [["abc", "def"], ["ghi", "jkl"]]
    assert longest_word(test_list) == "abc"  # Should return the first longest word encountered

def test_num_characters_single_character():
    test_list = [["a"], ["b", "c"]]
    assert num_characters(test_list) == 3