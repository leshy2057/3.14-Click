from .Notebooks import NotesList


class Player:
    def __init__(self):
        self.stats = {"money": 0, "languages": ["Unknown"], "soft": ["notepad"], "notebook": "Note"}

        self.notebook = NotesList.dictionaryNotes[self.stats["notebook"]]
        self.soft = NotesList.dictionaryNotes[self.stats["soft"]]
        self.notebook = NotesList.dictionaryNotes[self.stats["notebook"]]

