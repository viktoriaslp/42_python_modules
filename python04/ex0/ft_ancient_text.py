#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    vault: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {vault}")
    try:
        fd = open(vault, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    else:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        vault_data: str = fd.read()
        print(vault_data)
        print()
        fd.close()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
