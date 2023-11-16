"""File to define Fish class."""


class Fish:
    """Class - represents the fish."""
    
    age = int

    def __init__(self):
        """Fish Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase age + 1."""
        self.age += 1
        return None