class NotesList:
    def __init__(self):
        self.dictionaryNotes = {
            "Note": Notebook("Note", "None", 0, 1),
        }


class Notebook:
    def __init__(self, getName, getDescription, getPrice, getDamage):
        self.name = getName
        self.description = getDescription
        self.price = getPrice

        self.damage = getDamage


