#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")

    if not scores:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total_players: int = len(scores)
    total_scores: int = sum(scores)
    average: float = total_scores / total_players
    highest: int = max(scores)
    lowest: int = min(scores)
    score_range: int = highest - lowest

    print(
        f"Scores processed: {scores}\n"
        f"Total players: {total_players}\n"
        f"Total score: {total_scores}\n"
        f"Average score: {average}\n"
        f"High score: {highest}\n"
        f"Low score: {lowest}\n"
        f"Score range: {score_range}"
    )


if __name__ == "__main__":
    main()
