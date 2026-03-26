#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, growth: int = 1) -> None:
        self.height = self.height + growth

    def aged(self, aged: int = 1):
        self.age = self.age + aged

    def get_info(self):
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 80, 45)
    old_growth: int = rose.height

    print("=== Day 1 ===")
    rose.get_info()
    for day in range(6):
        rose.grow()
        sunflower.grow()
        rose.aged()
        sunflower.aged()

    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - old_growth}cm")
