#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name.capitalize()
        self.height: int = height
        self.age: int = age

    def get_comun_info(self) -> str:
        return (
            f"{self.name} ({self.__class__.__name__ }): "
            f"{self.height}cm, {self.age} days,"
        )


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self, blooming: bool) -> str:
        if blooming:
            return f"{self.name} is blooming beautifully!"
        else:
            return f"{self.name} is not blooming yet!"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self, square_meters: int) -> str:
        return f"Oak provides {square_meters} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants: list[Plant] = [
        Flower("rose", 25, 30, "red"),
        Tree("oak", 500, 1852, 50),
        Vegetable("tomato", 80, 90, "summer", "vitamin C"),
    ]

    print()
    for plant in plants:
        print(plant.get_comun_info(), end="")
        if plant.__class__.__name__ == "Flower":
            print(f" {plant.color} color")
            print(plant.bloom(True))
            print()
        elif plant.__class__.__name__ == "Tree":
            print(f" {plant.trunk_diameter}cm diameter")
            print(plant.produce_shade(78))
            print()
        elif plant.__class__.__name__ == "Vegetable":
            print(f" {plant.harvest_season} harvest")
            print(f"{plant.name} is rich in {plant.nutritional_value}")

    tulip: Plant = Flower("tulip", 15, 20, "purple")
    plants.append(tulip)
    pine: Plant = Tree("pine", 420, 1654, 40)
    plants.append(pine)
    broccoli: Plant = Vegetable("broccoli", 50, 153, "autumn", "B12")
    plants.append(broccoli)
