from abc import ABC, abstractmethod
import typing

class Creature(ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass


    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"