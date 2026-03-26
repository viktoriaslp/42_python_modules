#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    flowers: list[Plant] = []
    rose: Plant = Plant("rose", 25, 30)
    flowers.append(rose)
    sunflower: Plant = Plant("sunflower", 80, 45)
    flowers.append(sunflower)
    cactus: Plant = Plant("cactus", 15, 120)
    flowers.append(cactus)

    print("=== Garden Plant Registry ===")
    for flower in flowers:
        print(
            f"{flower.name.capitalize()}: "
            f"{flower.height}cm, {flower.age} days old"
        )
