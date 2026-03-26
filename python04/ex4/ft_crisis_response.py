#!/usr/bin/env python3


def crisis_handler(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            file_data: str = file.read()
    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Archive not found in storage matrix",
            "STATUS: Crisis handled, system stable",
            sep="\n"
        )
    except PermissionError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Security protocols deny access",
            "STATUS: Crisis handled, security maintained",
            sep="\n"
        )
    except Exception:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Unexpected anomaly detected in archive system"
            "STATUS: Crisis handled, system stable",
            sep="\n"
        )
    else:
        print(
            f"SUCCESS: Archive recovered - ``{file_data}''",
            "STATUS: Normal operations resumed",
            sep="\n"
        )


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    vaults_list: list[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for vault in vaults_list:
        crisis_handler(vault)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
