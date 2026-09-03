#!/usr/bin/env python3

import alchemy.transmutation
from alchemy.transmutation import (
    lead_to_gold,
    stone_to_gem,
    philosophers_stone,
    elixir_of_life,
)


def main() -> None:
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
