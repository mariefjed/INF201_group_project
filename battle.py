from character import Character


class Battle:
    """Manages turn-based combat between two Character objects."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Executes a single round where hero attacks enemy, and enemy attacks back if alive."""
        if self.hero.is_alive:
            self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> Character:
        """Simulates rounds in a loop until one character dies, returning the winner."""
        print(f"=== BATTLE START: {self.hero.name} VS {self.enemy.name} ===")
        round_num = 1

        while self.hero.is_alive and self.enemy.is_alive:
            print(f"\n--- Round {round_num} ---")
            self.play_round()
            print(f"Status: {self.hero.name} ({self.hero.hp} HP) | {self.enemy.name} ({self.enemy.hp} HP)")
            round_num += 1

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"\n Battle Over! Winner: {winner.name}!")
        return winner
    