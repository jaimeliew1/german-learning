from .cli import make_deck


def main() -> int:
    print("Hello from german-anki-deck!")
    make_deck()
    return 0
