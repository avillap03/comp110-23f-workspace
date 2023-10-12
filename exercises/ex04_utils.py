"""EX04 - List Utility Functions."""

__author__ = "730621663"


def all(input: list[int], given_int: int) -> bool:
    """Return a bool indicating wether or not all the ints in the list are the same as the given int"""
    if len(input) == 0:
        return False
    i: int = 0
    while int < len(input):
        if input[int] != given_int:
            return False
        i += 1
    return True 


def max(input: list[int]) -> int:
    """Return the largest int in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = input[i]
    while i < len(input):
        if max < input[i]:
            max = input[i]
        i += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return bool indicating if every element at every idx is equal in boths lists"""
    if list_1 == list_2:
        return True
    else: # list_1 != list_2
        return False
    