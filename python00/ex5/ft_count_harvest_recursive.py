# def ft_count_harvest_recursive(harvest: int = None, day: int = 1) -> None:
#     if harvest is None:
#         harvest = int(input("Days until harvest: "))

#     if day <= harvest:
#         print("Day", day)
#         ft_count_harvest_recursive(harvest, day + 1)
#     else:
#         print("Harvest time!")

def ft_recursive(harvest: int) -> None:
    if harvest > 0:
        ft_recursive(harvest - 1)
        print("Day", harvest)


def ft_count_harvest_recursive() -> None:
    harvest = int(input("Days until harvest: "))
    ft_recursive(harvest)
    print("Harvest time!")
