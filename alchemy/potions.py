from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    earth = create_earth()
    fire = create_fire()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    fire = create_fire()
    water = create_water()
    air = create_air()
    earth = create_earth()
    return f"Wisdompotion brewed with all elements: {fire, water, air, earth}"