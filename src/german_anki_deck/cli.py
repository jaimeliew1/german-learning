from pathlib import Path

import genanki
from rich import print
import random

from .models import GermanNouns, GermanVerbs
from .utils import int_to_german_spelling

IN_FN = Path(__file__).parent.parent.parent / "verbs.json"
NOUN_FN = Path(__file__).parent.parent.parent / "nouns_household.json"


def make_deck():
    with open(IN_FN, "r") as f:
        data = f.read()

    german_verbs = GermanVerbs.model_validate_json(data)
    verb_list = [verb.infinitive[1] for verb in german_verbs.verbs]
    anki_notes = german_verbs.anki_notes()
    print(f"Generating Anki deck ({len(anki_notes)} notes) for the following {len(verb_list)} verbs:")
    print(verb_list)

    my_deck = genanki.Deck(2059400110, "German verbs")

    for note in anki_notes:
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



def test_numbers():
    while True:
        x = random.randint(0, 100)
        print(x)
        input()
        print(int_to_german_spelling(x))
        
