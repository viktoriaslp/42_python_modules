#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_creation_info(self) -> None:
        print(
            f"Created: {self.name.capitalize()} "
            f"({self.height}cm, {self.age} days)"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_array = [
        ["rose", 25, 30],
        ["oak", 200, 365],
        ["cactus", 5, 90],
        ["sunflower", 80, 45],
        ["fern", 15, 120]
    ]

    plants: list[Plant] = []
    for plant in plants_array:
        plants.append(Plant(plant[0], plant[1], plant[2]))

    count = 0
    for plant in plants:
        count += 1
        plant.get_creation_info()

    print(f"\nTotal plants created: {count}")
