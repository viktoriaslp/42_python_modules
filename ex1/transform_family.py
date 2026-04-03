from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from ex1.transform_capability import TransformCapability
from ex1.heal_capability import HealCapability

class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.transformed = False

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> None:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"
    
    def revert(self) -> None:
        self.transformed = False
        return f"{self.name} returns to normal."   


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str):
        super().__init__(name, creature_type)
        self.transformed = False

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> None:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"
    
    def revert(self) -> None:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
