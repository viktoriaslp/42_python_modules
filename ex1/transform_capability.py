from abc import ABC, abstractmethod


class TransformCapability(ABC):    
    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass