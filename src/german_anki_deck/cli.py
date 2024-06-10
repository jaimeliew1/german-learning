from pathlib import Path

import genanki
from rich import print

from .models import GermanVerbs

IN_FN = Path(__file__).parent.parent.parent / "verbs.json"


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
