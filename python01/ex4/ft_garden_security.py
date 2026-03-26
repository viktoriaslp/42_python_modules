#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(
                f"Invalid operation attempted: height {height}cm [REJECTED]"
                f"\nSecurity: Negative height rejected"
                )

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            if age < 0:
                print("Security: Negative age rejected")

    def get_name(self) -> str:
        return self.__name.capitalize()

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("rose", 25, 30)
    print("Plant created:", plant.get_name())
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    print(
        f"Current plant: {plant.get_name()}"
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
