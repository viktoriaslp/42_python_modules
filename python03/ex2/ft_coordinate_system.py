import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
            "Enter new coordinates as float in format 'x,y,z': "
        )
        str_coordinates_list: list[str] = user_input.split(",")

        input_len: int = 0
        for _ in str_coordinates_list:
            input_len += 1

        if input_len != 3:
            print("Invalid syntax")
            continue
        coordinates_list: list[float] = []
        try:
            for element in str_coordinates_list:
                coordinates_list.append(float(element.strip()))
        except ValueError:
            print(
                f"Error on parameter '{element}': "
                f"could not convert string to float: '{element}'"
            )
            continue
        return (
            coordinates_list[0],
            coordinates_list[1],
            coordinates_list[2],
        )


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_t: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_t}")
    print(f"It includes: X={first_t[0]}, Y={first_t[1]}, Z={first_t[2]}")

    x1, y1, z1 = first_t
    distance_to_centre: float = math.sqrt((x1)**2 + (y1)**2 + (z1)**2)
    print(f"Distance to center: {round(distance_to_centre, 4)}\n")

    print("Get a second set of coordinates")
    second_t: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = second_t
    distance: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
