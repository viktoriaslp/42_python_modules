#!/usr/bin/env python3

import alchemy
import alchemy.elements


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}",
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}",
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}",
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}",
        sep="\n",
    )

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    print("alchemy.create_earth(): ", end="")
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
