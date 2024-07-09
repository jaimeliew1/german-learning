from pathlib import Path

import genanki
from pydantic import BaseModel

OUT_FN = Path(__file__).parent / "verbs.json"


class GermanVerb(BaseModel):
    infinitive: tuple[str, str]  # (English, German)
    conjugations: dict[
        str, tuple[str, str]
    ]  # A dictionary to hold conjugations (e.g., {'ich': ('I go', 'gehe'), ...})
    past_participle: tuple[str, str]  # (English, German)
    examples: list[tuple[str, str]] = []

    def anki_notes(self) -> list[genanki.Note]:
        notes = []
        # infinitive
        notes.append(genanki.Note(model=genanki.BASIC_MODEL, fields=self.infinitive))

        # conjugations
        for pronoun, (english, german) in self.conjugations.items():
            notes.append(
                genanki.Note(
                    model=genanki.BASIC_MODEL, fields=(english, pronoun + " " + german)
                )
            )

        # past participle
        notes.append(
            genanki.Note(
                model=genanki.BASIC_MODEL,
                fields=(self.past_participle[0], self.past_participle[1]),
            )
        )
        # examples
        for english, german in self.examples:
            notes.append(
                genanki.Note(model=genanki.BASIC_MODEL, fields=(english, german))
            )
        return notes


class GermanVerbs(BaseModel):
    verbs: list[GermanVerb]

    def anki_notes(self) -> list[genanki.Note]:
        notes = []
        for verb in self.verbs:
            notes.extend(verb.anki_notes())

        return notes


class GermanNoun(BaseModel):
    noun: tuple[str, str]
    examples: list[tuple[str, str]] = []

    def anki_notes(self) -> list[genanki.Note]:
        notes = []

        notes.append(genanki.Note(model=genanki.BASIC_MODEL, fields=self.noun))

        # examples
        for english, german in self.examples:
            notes.append(
                genanki.Note(model=genanki.BASIC_MODEL, fields=(english, german))
            )

        return notes


class GermanNouns(BaseModel):
    nouns: list[GermanNoun]

    def anki_notes(self) -> list[genanki.Note]:
        notes = []
        for noun in self.nouns:
            notes.extend(noun.anki_notes())

        return notes
