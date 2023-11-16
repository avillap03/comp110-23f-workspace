"""Defining a Class!"""

from __future__ import annotations

"""
think of a class definition as 
a "roadmap" for objects  that
belong to the class
you are defining the underlying structure
every instance of this class will have
"""

class Pizza:
    """This is my class to represent pizza!"""

    # attributes
    # syntax <name> : <type>
    size: str
    toppings: int
    gluten_free:  bool

    def __init__(self, size_inp: str, toppings_inp: int, gf_inp: bool):
        """Constructor"""
        self.size = size_inp
        self.toppings = toppings_inp
        self.gluten_free = gf_inp
        # returns self


    def price(self) -> float:
        """Method to compute price of pizza."""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += cost
        return cost


    def add_toppings(self, num_toppings: int):
        """Update existing pizza order with num_topp."""
        self.toppings += num_toppings

    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Make new pizza order using existing info."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings)