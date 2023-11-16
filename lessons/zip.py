"""Combining two lists into a dictionary."""

__author__ = "730621663"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Function to create new dictionary."""
    result: dict[str, int] = {}
    if len(keys) != len(values) or len(keys) == 0 or len(values) == 0:
        return (dict())
    else: 
        for i in range(len(keys)):
            result[keys[i]] = values[i]
        return result