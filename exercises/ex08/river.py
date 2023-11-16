"""File to define River class."""

__author__ = "730621663"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class - represents the river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove fish if age > 3 and bears if age > 5."""
        # Remove fish
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        # Remove bear
        new_bears = []
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)
        self.bears = new_bears
        return None

    def bears_eating(self) -> None:
        """For each bear, if there are at least 5 fish, the bear will eat 3 fish."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                bears.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self) -> None:
        """If hunger_score < 0, then remove the bear."""
        hunger = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                hunger.append(bears)
        self.bears = hunger
        return None
        
    def repopulate_fish(self) -> None:
        """Repopulate fish."""
        new_number_fish = (len(self.fish) // 2) * 4
        for fish in range(new_number_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self) -> None:
        """Repopulate Bear."""
        new_number_bears = len(self.bears) // 2
        for bears in range(new_number_bears):
            new_bears = Bear()
            self.bears.append(new_bears)
        return None
    
    def view_river(self) -> None:
        """Print river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bears in self.bears:
            bears.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Call one_river_day seven times."""
        for idx in range(7):
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Remove amount of fish."""
        for fish in range(amount):
            self.fish.pop(0)       
