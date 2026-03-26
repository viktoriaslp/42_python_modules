#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    arguments_number: int = len(sys.argv)
    if arguments_number == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arguments_number - 1}")
        count: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {count}: {arg}")
            count += 1
    print(f"Total arguments: {arguments_number}")


if __name__ == "__main__":
    main()
