from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        raise ValueError(
            f'Unknown operation: "{operation}".'
            ' Supported operations: "add", "multiply", "max", "min"')


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments: dict[str, Callable] = {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }
    return enchantments


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def main() -> None:
    spell_powers = [10, 20, 40, 30]
    fibonacci_tests = [0, 1, 10, 15]

    def enchantment(power: int, element: str, target: str) -> str:
        return f"Enchanted {target} with {element} for {power} power"

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print()

    print("Testing partial enchanter...")

    enchanter = partial_enchanter(enchantment)
    print(enchanter["fire"]("Sword"))
    print(enchanter["ice"]("Shield"))
    print()

    print("Testing memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher({"hello": 42}))


if __name__ == "__main__":
    main()
