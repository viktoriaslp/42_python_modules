#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    vault: str = "classified_data.txt"

    print("Initiating secure vault access...")
    try:
        with open(vault, "r") as file:
            print("Vault connection established with failsafe protocols\n")
            data: str = file.read()
            print("SECURE EXTRACTION:")
            print(data)
            print()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")

    new_vault: str = "security_protocols.txt"
    new_message: str = "[CLASSIFIED] New security protocols archived"
    with open(new_vault, "w") as file:
        print("SECURE PRESERVATION:")
        file.write(new_message)
        print(new_message)
    print("\nVault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
