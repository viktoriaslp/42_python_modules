import typing
from ex0 import FlameFactory, AquaFactory, CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    creatures = []
    try:
        creatures.append(factory.create_base())
        creatures.append(factory.create_evolved())
    except Exception:
        print("Invalid factory to create a creature")
    else:
        for creature in creatures:
            print(creature.describe())
            print(creature.attack())


def base_fight(f_factory: CreatureFactory, a_actory: CreatureFactory) -> None:
    fire_creature = f_factory.create_base()
    aqua_creature = a_actory.create_base()

    print(fire_creature.describe())
    print(" vs.")
    print(aqua_creature.describe())
    print(" fight!")
    
    print(fire_creature.attack())
    print(aqua_creature.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    testing_factory(flame_factory)
    print()
    print("Testing factory")
    testing_factory(aqua_factory)
    print()

    print("Testing battle")
    base_fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
  