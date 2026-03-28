#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.count: int = 0


    @abstractmethod
    # devuelve un resume textual
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    # devuelve una lista filtrada
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    # devuelve un diccionario
    def get_stats(self) -> Dict[str, Union[str, int, float]]: # what is the return value?
        return {
            "stream_id": self.stream_id,
            "type": "Generic Data",
            "count": self.count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"


    def process_batch(self, data_batch: List[str]) -> str:
        self.count: int = 0
        temp_count: int = 0
        temp_sum: float = 0
        for batch in data_batch:
            self.count += 1
            key, value = batch.split(":")
            if key == "temp":
                temp_count += 1
                try:
                    temp_sum += float(value)
                    avg_temp: float = temp_sum / temp_count
                except (ValueError, TypeError, ZeroDivisionError):
                    return f"Sensor analysis: {self.count} readings processed"
                else:
                    return (
                    f"Sensor analysis: {self.count} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                )
        return f"Sensor analysis: {self.count} readings processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]: # what is the return value?
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "count": self.count,
        }
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria != "high-priority":
            return data_batch

        return [
            item
            for item in data_batch
            if ":" in item and float(item.split(":")[1]) >= 60
        ]


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"


    def process_batch(self, data_batch: List[str]) -> str:
        self.count: int = 0
        net: int = 0
        for batch in data_batch:
            self.count += 1
            key, value = batch.split(":")
            if key == "sell":
                net -= int(value) # proteger con try?
            elif key == "buy":    
                net += int(value) # proteger con try?
        
        return (
            f"Transaction analysis: {self.count} operations, "
            f"net flow: {net:+} units"
        )


    def get_stats(self) -> Dict[str, Union[str, int, float]]: # what is the return value?
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "count": self.count,
        }
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria != "high-priority":
            return data_batch

        return [
            item
            for item in data_batch
            if ":" in item and float(item.split(":")[1]) > 100
        ]


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"


    def process_batch(self, data_batch: List[str]) -> str:
        error_count: int = 0
        self.count: int = 0
        for data in data_batch:
            self.count += 1
            if data == "error":
                error_count += 1
        
        return (
            f"Event analysis: {self.count} events, "
            f"{error_count} error detected"
        )


    def get_stats(self) -> Dict[str, Union[str, int, float]]: # what is the return value?
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "count": self.count,
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria != "high-priority":
            return data_batch

        return [
            item
            for item in data_batch
            if item == "error"
        ]


class StreamProcessor():
    
    def stream_batch_process(self, stream: DataStream, batch: List[Any]) -> str:
        stream.process_batch(batch)
        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {stream.count} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"- Transaction data: {stream.count} operations processed")
        elif isinstance(stream, EventStream):
            print(f"- Event data: {stream.count} events processed")


def main() -> None:

    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    trans_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    event_batch: List[str] = ["login", "error", "logout"]
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor_stream.process_batch(sensor_batch))
    print()

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    print(f"Processing transaction batch: {trans_batch}")
    print(transaction_stream.process_batch(trans_batch))
    print()

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(f"Processing event batch: {event_batch}")
    print(event_stream.process_batch(event_batch))
    print()

    print(
        "=== Polymorphic Stream Processing ===\n",
        "Processing mixed stream types through unified interface...\n"
    )
    
    stream_processor = StreamProcessor()
    mixed_batch: List[set[DataStream, List[str]]] = [
        (sensor_stream, ["humidity:63", "pressure:1011"]),
        (transaction_stream, ["buy:100", "buy:75", "buy:70", "buy:75"]),
        (event_stream, ["login", "error", "logout"]),
    ]
    
    print("Batch 1 Results:")
    for stream, data in mixed_batch:
        stream_processor.stream_batch_process(stream, data)
    print()

    filtered_sensor = sensor_stream.filter_data(sensor_batch, "high-priority")
    filtered_transaction = transaction_stream.filter_data(trans_batch, "high-priority")

    print("Stream filtering active: High-priority data only")

    sensor_count = 0
    for _ in filtered_sensor:
        sensor_count += 1

    transaction_count = 0
    for _ in filtered_transaction:
        transaction_count += 1

    print(
        f"Filtered results: {sensor_count} critical sensor alerts, "
        f"{transaction_count} large transaction"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
