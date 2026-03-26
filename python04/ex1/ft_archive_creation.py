#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    vault: str = "new_discovery.txt"

    print(f"Initializing new storage unit: {vault}")
    fd = open(vault, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    data_list: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    for line in data_list:
        fd.write(line + "\n")
        print(line)

    fd.close()
    print(
        "\nData inscription complete. Storage unit sealed.\n"
        f"Archive '{vault}' ready for long-term preservation."
    )


if __name__ == "__main__":
    main()
