from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from ex1.heal_capability import HealCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} Vine Whip!"

    def heal(self) -> None:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> None:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")

