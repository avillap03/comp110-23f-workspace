"""Summing the elements of a list using different loops."""

__author__ = "730621663" 


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in the list using a while loop."""
    total: float = 0.0
    idx: int = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in the list using a for loop."""
    total = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in the list using a for loop and a range."""
    total = 0.0
    for elem in range(len(vals)):
        total += vals[elem]
    return total