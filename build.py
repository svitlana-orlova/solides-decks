import os
import yaml
import genanki

def dump(uid, name, fin, fout):
    notes = []
    anki_model = genanki.Model(
        uid,
        name,
        fields = [
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates = [
            {
                'name': 'Card Note',
                'qfmt': '<strong>{{Question}}</strong>',
                'afmt': '{{FrontSide}}<hr id="answer"><strong>{{Answer}}</strong>',
            },
        ])

    with open(fin, 'r') as f:
        for line in f:
            notes.append(tuple(line.strip().split(';', 1)))

    anki_notes = [genanki.Note(
        model  = anki_model,
        fields = [question, answer]
    ) for question, answer in notes]

    anki_deck = genanki.Deck(uid, name)

    for note in anki_notes:
        anki_deck.add_note(note)

    genanki.Package(anki_deck).write_to_file(fout)
    pass

if __name__ == '__main__':

    settings = []

    with open('inputs.yaml', 'r') as file:
        settings = yaml.load(file, Loader=yaml.FullLoader)

    for deck in settings['data']:
        print("Generating deck: ", deck['name'])
        dump(deck['uid'], deck['name'], deck['input'], deck['output'])


