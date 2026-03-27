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
        return(f"Output: {result}")
    

class NumericProcessor(DataProcessor):
    def process(self, data: List[Union[int, float]]) -> str:
        numbers_count: int = 0
        numbers_sum: int = 0
        average: float = 0

        for number in data:
            numbers_count += 1
            numbers_sum += number

        average = numbers_sum / numbers_count

        return (
            f"Processed {numbers_count} numeric values, "
            f"sum={numbers_sum}, avg={average:.1f}"
        )


    def validate(self, data: List[Union[int, float]]) -> bool:
        if not data:
            return False
        for number in data:
            try:
                number = float(number)
            except (ValueError, TypeError):
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        words_count: int = 0
        char_count: int = 0

        words_list: List[str] = data.split()
        for word in words_list:
            words_count += 1

        for letter in data:
            char_count += 1

        return (
            f"Processed text: {char_count} characters, {words_count} words"
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


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        data_list: List[str] = data.split(":")
        log_level: str = data_list[0].strip()
        log_message: str = data_list[1].strip()

        if log_level == "ERROR":
            return (
                f"[ALERT] {log_level} level detected: {log_message}"
            )
        elif log_level == "INFO":
            return (
                f"[INFO] {log_level} level detected: {log_message}"
            )
        else:
            return (
                f"[LOG] {log_level} level detected: {log_message}"
            )


    def validate(self, data: str) -> bool:
        if not data:
            return False
        try:
            data_list: List[str] = data.split(":")
        except AttributeError:
            return False
        else:
            count: int = 0
            for word in data_list:
                word.strip()
                count += 1
            
            if count == 2 and data_list[0].isupper():
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
        print ("Validation: Numeric data verified")
        processed_data = numeric_processor.process(numeric_data)
        print(numeric_processor.format_output(processed_data))

    print()
    print(
        "Initializing Text Processor...",
        f'Processing data: "{text_data}"',
        sep="\n"
    )
    if text_processor.validate(text_data):
        print ("Validation: Text data verified")
        processed_data = text_processor.process(text_data)
        print(text_processor.format_output(processed_data))

    print()
    print(
        "Initializing Log Processor...",
        f'Processing data: "{log_data}"',
        sep="\n"
    )
    if log_processor.validate(log_data):
        print ("Validation: Log entry verified")
        processed_data = log_processor.process(log_data)
        print(log_processor.format_output(processed_data))

    print("\n=== Polymorphic Processing Demo ===\n")
    demo_data: List[DataProcessor] = [
        (NumericProcessor(), [1, 2, 3,]),
        (TextProcessor(), "Hello  World"),
        (LogProcessor(), "INFO: System ready"),
    ]

    print("Processing multiple data types through same interface...")
    for processor, data in demo_data:
        if processor.validate(data):
            print(processor.format_output(processor.process(data)))

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
