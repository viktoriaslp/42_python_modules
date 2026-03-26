#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        GardenError.__init__(self, message)


def garden_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as error:
        print(f"Caught {type(error).__name__}: {error}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as error:
        print(f"Caught {type(error).__name__}: {error}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_errors()
