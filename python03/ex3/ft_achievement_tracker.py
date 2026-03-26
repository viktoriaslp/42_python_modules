import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder"
    ]

    amount: int = random.randint(3, 10)
    return set(random.sample(achievements, amount))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    print(
        f"Player Alice: {alice}\n"
        f"Player Bob: {bob}\n"
        f"Player Charlie: {charlie}\n"
        f"Player Dylan: {dylan}"
    )

    distincts: set[str] = alice.union(bob).union(charlie).union(dylan)
    print(f"\nAll distinct achievements: {distincts}")

    common_achievements: set[str] = (
        alice
        .intersection(bob)
        .intersection(charlie)
        .intersection(dylan)
    )
    print(f"\nCommon achievements: {common_achievements}\n")

    alice_unique = alice.difference(bob).difference(charlie).difference(dylan)
    bob_unique = bob.difference(alice).difference(charlie).difference(dylan)
    char_unique = charlie.difference(bob).difference(alice).difference(dylan)
    dylan_unique = dylan.difference(bob).difference(charlie).difference(alice)

    print(
        f"Only Alice has: {alice_unique}",
        f"Only Bob has: {bob_unique}",
        f"Only Charlie has: {char_unique}",
        f"Only Dylan has: {dylan_unique}",
        sep="\n"
    )

    alice_missing = distincts.difference(alice)
    bob_missing = distincts.difference(bob)
    charlie_missing = distincts.difference(charlie)
    dylan_missing = distincts.difference(dylan)

    print(
        "\n"
        f"Alice is missing: {alice_missing}",
        f"Bob is missing: {bob_missing}",
        f"Charlie is missing: {charlie_missing}",
        f"Dylan is missing: {dylan_missing}",
        sep="\n"
    )


if __name__ == "__main__":
    main()
