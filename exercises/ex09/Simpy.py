"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730621663"


class Simpy:
    """Utility class for working with a column of numerical values."""
    values: list[float]

    def __init__(self, inp_values: list[float] = []):
        """Constructor for Simpy."""
        self.values = inp_values

    def __str__(self) -> str:
        """Str Method - turn float values into str."""
        return f"Simpy({self.values})"
    
    def fill(self, values: float, count: int) -> None:
        """Fill Simpy values with a specific numnber of repeating values."""
        self.values = [values] * count

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in Simpy values attribute with range of values."""
        assert step != 0.0
        num = start
        while (step > 0 and num < stop) or (step < 0 and num > stop):
            self.values.append(num)
            num += step

    def sum(self) -> float:
        """Return the sum of all items in the values attribute."""
        total: float = 0.0
        for item in self.values:
            total += item
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allow addition of Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs.values[item])
        return result 
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allow power opperator for Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs.values[item])
        return result 
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows the use of equal sign between Simpy objects."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                if self.values[item] == rhs.values[item]:
                    result.append(True)
                else: 
                    result.append(False)
        return result 
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows the use of greater than sign between Simpy objects."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                if self.values[item] > rhs.values[item]:
                    result.append(True)
                else: 
                    result.append(False)
        return result 
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]: 
        """Allows the use of subscription operator between Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            if rhs > len(self.values):
                raise IndexError
            result: float = self.values[rhs]
            return result
        else: 
            for item in range(len(self.values)):
                if rhs[item] is True:
                    result.values.append(self.values[item])
            return result
        
        