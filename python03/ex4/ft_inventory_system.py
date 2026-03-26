import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    key_value: list[str] = []
    for arg in sys.argv[1:]:
        key_value = arg.split(":")
        if len(key_value) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key_value[0] not in inventory:
            try:
                inventory.update({key_value[0]: int(key_value[1])})
            except ValueError as error:
                print(f"Quantity error for '{key_value[0]}': {error}")
                continue
        else:
            print(f"Redundant item '{key_value[0]}' - discarding")
            continue

    if len(inventory) == 0:
        print(
            "No items provided. "
            "Usage: python3 ft_inventory_system.py <item_name>:<quantity> ..."
        )
    else:
        items_number: int = len(inventory)
        total_count: int = sum(inventory.values())

        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {items_number} items: {total_count}")
        for item in inventory:
            print(
                f"Item {item} "
                f"represents {round(inventory[item] / total_count * 100, 1)}%"
            )

        highest: int = 0
        highest_key: str = ""
        lowest: int = 2147483647
        lowest_key: str = ""

        for key in inventory.keys():
            if inventory[key] > highest:
                highest = inventory[key]
                highest_key = key
            if inventory[key] < lowest:
                lowest = inventory[key]
                lowest_key = key

        print(
            f"Item most abundant: {highest_key} with quantity {highest}\n"
            f"Item least abundant: {lowest_key} with quantity {lowest}"
        )
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
