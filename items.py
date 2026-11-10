from dice import Dice


class Weapon:
    """Represents a weapon equipped with a damage dice."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls damage using the weapon's damage dice."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', damage_dice={self.damage_dice})"

    def __str__(self) -> str:
        return f"{self.name} (Damage Dice: {self.damage_dice})"
    