#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        Exception.__init__(self, message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(
            f"Caught PlantError: Invalid plant name to water: '{plant_name}'"
        )


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")

    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(error)
        return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
