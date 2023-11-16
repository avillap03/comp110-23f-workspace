"""File to define Bear class."""


class Bear:
    """Class - pepresents the bears."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Bear Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increase  age and decrease hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Update Bears hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
        return None