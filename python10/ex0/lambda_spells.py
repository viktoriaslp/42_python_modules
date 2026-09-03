def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(mages, key=lambda mage: mage["power"])["power"]
    min_power: int = min(mages, key=lambda mage: mage["power"])["power"]

    total_power: int = sum(map(lambda mage: mage["power"], mages))
    avg_power: float = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'relic'},
        {'name': 'Lightning Rod', 'power': 60, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 75, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]

    spells = ['tsunami', 'freeze', 'lightning', 'blizzard']

    mages = [
        {'name': 'Alex', 'power': 74, 'element': 'lightning'},
        {'name': 'Nova', 'power': 99, 'element': 'earth'},
        {'name': 'Sage', 'power': 77, 'element': 'light'},
        {'name': 'Ember', 'power': 60, 'element': 'earth'},
        {'name': 'Alex', 'power': 55, 'element': 'earth'}
    ]

    print("\nTesting artifact sorter...")
    sorted_a = artifact_sorter(artifacts)
    print(
        f'{sorted_a[0]["name"]} ({sorted_a[0]["power"]} power)',
        f'comes before {sorted_a[1]["name"]} ({sorted_a[1]["power"]} power)'
    )

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 66)
    print(f"Filtered mages: {len(filtered_mages)}/{len(mages)}")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f'Max Power: {stats["max_power"]}')
    print(f'Min Power: {stats["min_power"]}')
    print(f'Average Power: {stats["avg_power"]}')


if __name__ == "__main__":
    main()
