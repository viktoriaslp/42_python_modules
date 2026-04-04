from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"
