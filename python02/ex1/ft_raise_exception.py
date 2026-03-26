#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except ValueError as error:
        raise ValueError(f"Caught input_temperature error: {error}")
    if temperature < 0:
        raise ValueError(
            "Caught input_temperature error:"
            f" {temp_str}°C is too hot for plants (max 40°C)"
        )
    elif temperature > 40:
        raise ValueError(
            "Caught input_temperature error:"
            f"{temp_str}°C is too cold for plants (min 0°C)"
        )
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    temperatures: list[str] = ["25", "abc", "100", "-50"]
    for temperature in temperatures:
        print(f"Input data is '{temperature}'")
        try:
            checked_temp: int = input_temperature(temperature)
            print(f"Temperature is now {checked_temp}°C\n")
        except ValueError as error:
            print(error)
            print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
