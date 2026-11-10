import random


class Dice:
    """Represents an n-sided die for random value generation."""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("A die must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Rolls the die and returns a random integer between 1 and sides."""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Allows rolling the die by calling the instance directly (e.g. d20())."""
        return self.roll()

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"
    