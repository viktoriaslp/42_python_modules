#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"{result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Union[List[int], List[float]]) -> str:
        numbers_count: int = 0
        numbers_sum: float = 0
        average: Optional[float] = 0

        for number in data:
            numbers_count += 1
            numbers_sum += number
        try:
            average = numbers_sum / numbers_count
        except (ZeroDivisionError, AttributeError):
            return "0 numeric values, sum=0, avg=0.0"

        return (
            f"{numbers_count} numeric values, "
            f"sum={numbers_sum}, avg={average:.1f}"
        )

    def validate(self, data: Union[List[int], List[float]]) -> bool:
        if not data:
            return False
        for number in data:
            try:
                number = float(number)
            except (ValueError, TypeError):
                return False
        return True

    def format_output(self, result: str) -> str:
        base: str = super().format_output(result)
        return (f"Processed {base}")


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        words_count: int = 0
        char_count: int = 0

        words_list: List[str] = data.split()
        for _ in words_list:
            words_count += 1

        for _ in data:
            char_count += 1

        return (
            f"text: {char_count} characters, {words_count} words"
        )

    def validate(self, data: str) -> bool:
        if not data:
            return False
        try:
            data.split()
        except AttributeError:
            return False
        else:
            return True

    def format_output(self, result: str) -> str:
        base: str = super().format_output(result)
        return (f"Processed {base}")


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            data_list: List[str] = data.split(":")
            log_data: Dict[str, str] = {
                "level": data_list[0].strip(),
                "message": data_list[1].strip()
            }
            if log_data["level"] == "ERROR":
                return (
                    f"[ALERT] {log_data['level']} "
                    f"level detected: {log_data['message']}"
                )
            elif log_data["level"] == "INFO":
                return (
                    f"[INFO] {log_data['level']} "
                    f"level detected: {log_data['message']}"
                )
            else:
                return (
                    f"[LOG] {log_data['level']} "
                    f"level detected: {log_data['message']}"
                )
        except (IndexError, AttributeError):
            return "Invalid data for LogProcessor to proces"

    def validate(self, data: str) -> bool:
        if not data:
            return False
        try:
            data_list: List[str] = data.split(":")
        except AttributeError:
            return False
        else:
            count: int = 0
            for _ in data_list:
                count += 1

            if count == 2 and data_list[0].strip().isupper():
                return True
            return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    text_data: str = "Hello Nexus World"
    log_data: str = "ERROR: Connection timeout"

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print()
    print(
        "Initializing Numeric Processor...",
        f"Processing data: {numeric_data}",
        sep="\n"
    )
    if numeric_processor.validate(numeric_data):
        print("Validation: Numeric data verified")
        processed_data = numeric_processor.process(numeric_data)
        print("Output:", numeric_processor.format_output(processed_data))

    print()
    print(
        "Initializing Text Processor...",
        f'Processing data: "{text_data}"',
        sep="\n"
    )
    if text_processor.validate(text_data):
        print("Validation: Text data verified")
        processed_data = text_processor.process(text_data)
        print("Output:", text_processor.format_output(processed_data))

    print()
    print(
        "Initializing Log Processor...",
        f'Processing data: "{log_data}"',
        sep="\n"
    )
    if log_processor.validate(log_data):
        print("Validation: Log entry verified")
        processed_data = log_processor.process(log_data)
        print("Output:", log_processor.format_output(processed_data))

    print("\n=== Polymorphic Processing Demo ===\n")
    demo_data: List[tuple[DataProcessor, Any]] = [
        (NumericProcessor(), [1, 2, 3,]),
        (TextProcessor(), "Hello  World"),
        (LogProcessor(), "INFO: System ready"),
    ]

    print("Processing multiple data types through same interface...")
    count: int = 1
    for processor, data in demo_data:
        if processor.validate(data):
            print(f"Result {count}: ", end="")
            print(processor.format_output(processor.process(data)))
            count += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
