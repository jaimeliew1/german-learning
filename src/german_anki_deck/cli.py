from pathlib import Path

import genanki
from rich import print

from .models import GermanNouns, GermanVerbs

IN_FN = Path(__file__).parent.parent.parent / "verbs.json"
NOUN_FN = Path(__file__).parent.parent.parent / "nouns_household.json"


def make_deck():
    with open(IN_FN, "r") as f:
        data = f.read()

    german_verbs = GermanVerbs.model_validate_json(data)
    verb_list = [verb.infinitive[1] for verb in german_verbs.verbs]
    print(f"Generating Anki deck for the following {len(verb_list)} verbs:")
    print(verb_list)

    my_deck = genanki.Deck(2059400110, "German verbs")

    for note in german_verbs.anki_notes():
        my_deck.add_note(note)

    genanki.Package(my_deck).write_to_file("output.apkg")


def make_noun_deck():
    with open(NOUN_FN, "r") as f:
        data = f.read()

    german_nouns = GermanNouns.model_validate_json(data)
    noun_list = [noun.noun[1] for noun in german_nouns.nouns]
    print(f"Generating Anki deck for the following {len(noun_list)} nouns:")
    print(noun_list)

    my_deck = genanki.Deck(2059400111, "German nouns (household)")

    for note in german_nouns.anki_notes():
        my_deck.add_note(note)

    genanki.Package(my_deck).write_to_file("output_nouns_household.apkg")
