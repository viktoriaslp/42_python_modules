from typing import List
from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability
from ex1.heal_capability import HealCapability
from ex2.exceptions import InvalidStrategy


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}' "
                "for this normal strategy"
            )
        else:
            return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}' "
                "for this agressive strategy"
            )
        else:
            return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        else:
            return [creature.attack(), creature.heal()]
