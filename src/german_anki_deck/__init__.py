from .cli import make_deck, make_noun_deck


def main() -> int:
    print("Hello from german-anki-deck!")
    make_deck()
    make_noun_deck()
    return 0
