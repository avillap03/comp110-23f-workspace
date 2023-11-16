"""Test my zip function."""

__author__ = "730621663"

from lessons.zip import zip


def test_empty_list() -> None:
    """Edge case test - zip with empty inputs - return empty dictionary."""
    assert zip([], []) == {}


def test_same_length_list() -> None:
    """Use case test - zip with two lists of the same length - return dictionary with keys and values."""
    keys = ["a", "b"]
    values = [1, 2]
    assert zip(keys, values) == {"a": 1, "b": 2}


def test_different_length_list() -> None:
    """Test zip with two lists of different lenghts - return empty dictionary."""
    keys = ["a", "b", "c"]
    values = [1, 2]
    assert zip(keys, values) == {}
