from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell1 and spell2 must be callable")

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be callable")

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("condition and spell must be callable")

    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    for spell in spells:
        if not callable(spell):
            raise TypeError("all spells must be callable")

    def cast_spells(target: str, power: int) -> list[str]:
        spell_results = []
        for spell in spells:
            spell_results.append(spell(target, power))
        return spell_results
    return cast_spells


def main() -> None:
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def can_kill(target: str, power: int) -> bool:
        return target == 'Dragon' and power > 4

    print("\nTesting spell combiner...")
    print("Combined spell result: ", end="")
    combined_spell = spell_combiner(fireball, heal)
    print(", ".join(combined_spell('Dragon', 4)))

    print("\nTesting power amplifier...")
    target = 'Wizard'
    power = 10
    amplifier = power_amplifier(fireball, 3)
    print(f"Original: {fireball(target, power)}")
    print(f"Amplified: {amplifier(target, power)}")

    print("\nTesting conditional caster...")
    casted_spell = conditional_caster(can_kill, fireball)
    print(f"Case True: {casted_spell('Dragon', 6)}")
    print(f"Case False: {casted_spell('Knight', 3)}")

    print("\nTesting spell sequence...")
    sequenced = spell_sequence([fireball, heal, fireball, heal])
    print("\n".join(sequenced('Goblin', 9)))


if __name__ == "__main__":
    main()
