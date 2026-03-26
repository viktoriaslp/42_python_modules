#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        try:
            print(int("abc"))
        except ValueError as error:
            raise ValueError(f"Caught ValueError: {error}")
    elif operation_number == 1:
        try:
            print(9 / 0)
        except ZeroDivisionError:
            raise ZeroDivisionError(
                "Caught ZeroDivisionError: division by zero"
            )
    elif operation_number == 2:
        try:
            file_name = "non/existant/file"
            open(file_name)
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"Caught FileNotFoundError: {error}"
            )
    elif operation_number == 3:
        try:
            string: str = "hello"
            number: int = 42
            print(string + number)
        except TypeError as e:
            raise TypeError(f"Caught TypeError: {e}")
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for case in range(5):
        print(f"Testing operation {case}...")
        try:
            garden_operations(case)
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
        ) as error:
            print(f"{error}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_types()
