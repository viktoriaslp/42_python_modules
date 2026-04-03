from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability
from ex1.heal_capability import HealCapability

class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass
    
    @abstractmethod
    def act(self, creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, Creature)
    
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategy(f"Invalid Creature '{creature}' for this normal strategy")
        else:
            return [creature.attack()]

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategy(f"Invalid Creature '{creature}' for this aggtessive strategy")
        else:
            return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategy(f"Invalid Creature '{creature}' for this defensive strategy")
        else:
            return [creature.attack(), creature.heal()]