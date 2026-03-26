import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    events = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release"
    ]

    while True:
        yield (random.choice(players), random.choice(events))


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        one_element: tuple[str, str] = random.choice(events)
        events.remove(one_element)
        yield one_element


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    events_list: list[tuple[str, str]] = []
    for _ in range(10):
        events_list.append(next(generator))

    print(f"Built list of 10 events: {events_list}")
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
