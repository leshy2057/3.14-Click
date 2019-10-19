from __future__ import absolute_import

from .Notebooks import NotesList
from .Soft import ProgrammsList
from .Languages import LanguagesList


class Player:
    def __init__(self):
        self.stats = {"money": 1000, "languages": ["Unknown", 0], "soft": ["notepad"], "notebook": "Note"}
        self.damage = 0
        self.UpdateStats()
    
    def UpdateStats(self):
        self.notebook = NotesList.dictionaryNotes[self.stats["notebook"]]
        self.soft = ProgrammsList.dictionarySoft[self.stats["soft"][0]]
        self.language = LanguagesList.dictionaryLanguages[self.stats["languages"][0]]

        self.damage = self.notebook.damage + self.soft.damage + self.language.levelsKnow[self.stats["languages"][1]]["damage"]
    
    def BuyNewNotebook(self):
        num = NotesList.listNotes.index(self.stats["notebook"])

        if (num + 1 < len(NotesList.listNotes)):
            if (self.stats["money"] - NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].price >= 0):
                self.stats["notebook"] = NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].name
                self.stats["money"] -= NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].price
                self.UpdateStats()

    def UpdateLevelLanguage(self):
        pass



