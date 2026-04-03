from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple(CreatureFactory, BattleStrategy)]) -> None:
    for opponent in opponents:
        pass


def main() -> None:
    fire_creature = f_factory.create_base()
    aqua_creature = a_actory.create_base()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    battle_one = [(Flameling, Normal), (Healing, Defensive)]
    battle_two = [(Flameling, Aggressive), (Healing, Defensive)]
    battle_three = [(Aquabub, Normal), (Healing, Defensive), (Transform, Aggressive)]

    

if __name__ == "__main__":
    main()
  