#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self, increase: int = 1) -> None:
        self.height += increase
        print(f"{self.name} grew {increase}cm")

    def print_details(self) -> str:
        return ""


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color

    def print_details(self) -> str:
        return f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points: int = points

    def print_details(self) -> str:
        return (
            f", {self.color} flowers (blooming), "
            f"Prize points: {self.points}"
        )


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name.capitalize()
        self.plants: list[Plant] = []
        self.plants_added: int = 0
        self.plants_growth: int = 0

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        self.plants_added += 1
        return f"Added {plant.name} to {self.name}'s garden"

    def grow_plants(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.plants_growth += 1

    def plants_available(self) -> int:
        print("Plants in garden:")
        count: int = 0
        for plant in self.plants:
            count += 1
            print(
                f"- {plant.name}: {plant.height}cm",
                plant.print_details(), sep=""
            )
        return count


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(
        cls,
        names: list[str] | None = None
    ) -> "GardenManager":
        if names is None:
            names = []
        manager = cls()
        for name in names:
            manager.add_garden(Garden(name))
        return manager

    def count_gardens(self) -> int:
        count: int = 0
        for garden in self.gardens:
            count += 1
        return count

    @staticmethod
    def height_validation(height: int) -> bool:
        return height > 0

    class GardenStats:
        @staticmethod
        def calculate_score(plants: list[Plant]) -> int:
            total_score: int = 0

            for plant in plants:
                total_score += plant.height
                if isinstance(plant, PrizeFlower):
                    total_score += (plant.points * 4)

            return total_score

        @staticmethod
        def calculate_types(plants: list[Plant]) -> tuple[int, int, int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1

            return regular, flowering, prize


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager: GardenManager = GardenManager.create_garden_network(
        ["Alice", "Bob"]
        )
    alice: Garden = manager.gardens[0]
    bob: Garden = manager.gardens[1]

    print(alice.add_plant(Plant("Oak Tree", 100)))
    print(alice.add_plant(FloweringPlant("Rose", 25, "red")))
    print(alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10)))
    bob.add_plant(Plant("Cactus", 92))

    print()
    alice.grow_plants()
    print()

    print("=== Alice's Garden Report ===")
    alice.plants_available()
    print()
    print(
        f"Plants added: {alice.plants_added}, "
        f"Total growth: {alice.plants_growth}cm"
        )

    regular: int
    flowering: int
    prize: int

    regular, flowering, prize = (
        GardenManager.GardenStats.calculate_types(alice.plants)
    )
    print(
        f"Plant types: {regular} regular, "
        f"{flowering} flowering, {prize} prize flowers"
    )
    print()
    result = True
    for plant in alice.plants:
        if not GardenManager.height_validation(plant.height):
            result = False
    print(f"Height validation test: {result}")

    alice_score = GardenManager.GardenStats.calculate_score(alice.plants)
    bob_score = GardenManager.GardenStats.calculate_score(bob.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.count_gardens()}")
