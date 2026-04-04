from abc import ABC, abstractmethod


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
