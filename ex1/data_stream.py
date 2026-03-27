#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass


    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass


    def get_stats(self) -> Dict[str, Union[str, int, float]]: # what is the return value?
        pass


class SensorStream(DataStream):
    ...


class TransactionStream(DataStream):
    ...


class EventStream(DataStream):
    ...


class StreamProcessor():
    if isinstance(value, SensorStream):
        pass
    elif isinstance(value, TransactionStream):
        pass
    elif isinstance(value, EventStream):
        pass



if __name__ == "__main__":
    main()
