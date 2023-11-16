"""testing my sum of evens function"""

from lessons.sum_evens import sum_evens_of_lists

def test_empty_list() -> None:
    """sum_evens_of list([]) should return 0"""
    assert sum_evens_of_lists([]) == 0


def test_sum_one_element() -> None:
    """sum_evens_of_list([2]) = 2"""
    test_list: list[int] = [2]
    assert sum_evens_of_lists(test_list) == 2


def test_sum_positives() -> None:
    """sum_evens_of_list of a list of positive number"""
    test_list: list[int] = [1,2,3,4]
    assert sum_evens_of_lists(test_list) == 6


def test_sum_neg_and_pos() -> None:
    """sum_evens_of_list of a list with negatives and positives"""
    test_list: list[int] = [-1,-2,3,4]
    assert sum_evens_of_lists(test_list) == 2