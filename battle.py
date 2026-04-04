from ex0.creature_factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory


def testing_factory(factory: CreatureFactory) -> None:
    creatures = []
    creatures.append(factory.create_base())
    creatures.append(factory.create_evolved())

    for creature in creatures:
        print(creature.describe())
        print(creature.attack())


def base_fight(fire_factory: CreatureFactory, aqua_actory: CreatureFactory) -> None:
    fire_creature = fire_factory.create_base()
    aqua_creature = aqua_actory.create_base()

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
