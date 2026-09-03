from collections.abc import Callable


def mage_counter() -> Callable:
    increase: int = 0

    def count() -> int:
        nonlocal increase
        increase += 1
        return increase

    return count


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(add_power: int) -> int:
        nonlocal initial_power
        initial_power += add_power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item: str) -> str:
        return enchantment_type + " " + item

    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        if key in memory:
            return memory[key]
        return "Memory not found"

    functions_dict: dict[str, Callable] = {
        "store": store,
        "recall": recall
    }

    return functions_dict


def main() -> None:
    enchantment_types = ['Shocking', 'Frozen', 'Flaming']

    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()

    accumulate = spell_accumulator(100)
    print("Testing spell accumulator...")
    print(f"Base 100, add 20: {accumulate(20)}")
    print(f"Base 100, add 30: {accumulate(30)}")
    print()

    enchantment1 = enchantment_factory(enchantment_types[2])
    enchantment2 = enchantment_factory(enchantment_types[1])
    print("Testing enchantment factory...")
    print(enchantment1('Sword'))
    print(enchantment2('Shield'))
    print()

    key = 'secret'
    value = 42
    vault = memory_vault()
    store_func = vault['store']
    recall_func = vault['recall']

    print("Testing memory vault...")
    print(f"Store {key} = {value}")
    store_func(key, value)
    print(f"Recall {key}: {recall_func(key)}")
    print(f"Recall 'unknown': {recall_func('unknown')}")


if __name__ == "__main__":
    main()
