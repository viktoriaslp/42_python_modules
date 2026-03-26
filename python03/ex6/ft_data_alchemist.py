import random


def main() -> None:
    players: list[str] = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")

    players_capit: list[str] = [
        player.capitalize() for player in players
    ]
    print(f"New list with all names capitalized: {players_capit}")

    only_capital: list[str] = [
        player for player in players if player == player.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capital}")

    score_dict: dict[str, int] = {
        player: random.randint(1, 1000) for player in players_capit
    }
    print(f"Score dict: {score_dict}")

    average: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    best_players: dict[str, int] = {
        key: score_dict[key] for key in score_dict if score_dict[key] > average
    }
    print(f"High scores: {best_players}")


if __name__ == "__main__":
    main()
