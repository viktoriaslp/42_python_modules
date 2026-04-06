from typing import List, Tuple
from ex0.creature_factory import CreatureFactory
from ex2.battle_strategy import BattleStrategy
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategy,
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i, first in enumerate(opponents):
        for second in opponents[i + 1:]:
            factory_one, strategy_one = first
            factory_two, strategy_two = second

            creature_one = factory_one.create_base()
            creature_two = factory_two.create_base()

            print("* Battle *")
            print(creature_one.describe())
            print(" vs.")
            print(creature_two.describe())
            print(" now fight!")
            try:
                for act in strategy_one.act(creature_one):
                    print(act)
                for act_two in strategy_two.act(creature_two):
                    print(act_two)
            except InvalidStrategy as error:
                print(f"Battle error, aborting tournament: {error}")
                return
            print()


def main() -> None:

    battle_one = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle_two = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle_three = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(battle_one)} opponents involved\n")
    battle(battle_one)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(battle_two)} opponents involved\n")
    battle(battle_two)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(battle_three)} opponents involved\n")
    battle(battle_three)


if __name__ == "__main__":
    main()
