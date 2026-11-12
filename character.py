from typing import Optional

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Optional[Weapon] = None,
    ) -> None:
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property returning True if character's HP is greater than 0."""
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
        """Reduces the character's own HP by the damage amount. HP cannot drop below 0."""
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        """Increases character's HP by amount, capped at max HP."""
        if self.is_alive:
            self._hp = min(self.hp_max, self._hp + amount)

    def attack(self, target: "Character") -> None:
        """Attacks target character. Uses weapon damage if equipped, otherwise base damage."""
        if not self.is_alive:
            print(f"{self.name} cannot attack because they are defeated!")
            return

        if self.weapon is not None:
            dmg = self.weapon.roll_damage()
            print(
                f"{self.name} attacks {target.name} with {self.weapon.name} for"
                f" {dmg} damage!"
            )
        else:
            dmg = self.damage
            print(f"{self.name} attacks {target.name} for {dmg} damage!")

        target.take_damage(dmg)

    def introduce(self) -> None:
        """Creates string that introduces character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        return (
            f"<Character name={self.name} hp={self.hp} damage={self.damage}"
            f" weapon={self.weapon}>"
        )

    def __str__(self) -> str:
        return (
            f"Character: {self.name} with {self.hp} HP and {self.damage} damage"
        )


class Warrior(Character):
    """Warrior subclass specialized in defense."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Optional[Weapon] = None,
        armor: int = 5,
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Overrides take_damage: reduces incoming damage by armor value before applying it."""
        effective_damage = max(0, amount - self.armor)
        super().take_damage(effective_damage)

    def __repr__(self) -> str:
        return (
            f"Warrior name={self.name} hp={self.hp}/{self.hp_max}"
            f" armor={self.armor} weapon={self.weapon}"
        )


class Mage(Character):
    """Mage subclass relying on mana for magic attacks."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Optional[Weapon] = None,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = mana

    def attack(self, target: Character) -> None:
        """Overrides attack: spends 10 mana for double magic damage, or falls back to base/weapon attack and recovers 5 mana."""
        if not self.is_alive:
            print(f"{self.name} cannot attack because they are defeated!")
            return

        if self.mana >= 10:
            self.mana -= 10
            spell_damage = self.damage * 2
            print(
                f"{self.name} casts a Magic Spell on {target.name} dealing"
                f" {spell_damage} magic damage! (Mana left: {self.mana})"
            )
            target.take_damage(spell_damage)
        else:
            print(
                f"{self.name} has low mana ({self.mana}/{self.mana_max}) and"
                " recovers 5 mana!"
            )
            self.mana = min(self.mana_max, self.mana + 5)
            super().attack(target)

    def __repr__(self) -> str:
        return (
            f"<Mage name={self.name} hp={self.hp}/{self.hp_max}"
            f" mana={self.mana}/{self.mana_max} weapon={self.weapon}>"
        )