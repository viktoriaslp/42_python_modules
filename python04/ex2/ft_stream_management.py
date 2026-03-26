#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    collected_id: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")

    print()
    print(
        f"[STANDARD] Archive status from {collected_id}: "
        f"{report}", file=sys.stdout
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print()
    print("Three-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    main()
