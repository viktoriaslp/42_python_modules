from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def validator(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            elif args and isinstance(args[0], int):
                power = args[0]
            else:
                power = args[-1]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {i}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not all(c.isalpha() or c == " " for c in name):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    @retry_spell(3)
    def failure_spell() -> str:
        raise ValueError("Spell failed")

    @retry_spell(3)
    def successful_spell() -> str:
        return "Waaaaaaagh spelled !"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print()

    print("Testing retrying spell...")
    print(failure_spell())
    print(successful_spell())
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Luna"))
    print(MageGuild.validate_mage_name("L43"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))


if __name__ == "__main__":
    main()
