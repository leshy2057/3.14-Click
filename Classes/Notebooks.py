class Notebook:
    def __init__(self, getName, getDescription, getPrice, getDamage):
        self.name = getName
        self.description = getDescription
        self.price = getPrice

        self.damage = getDamage



class NotesList:
    dictionaryNotes = {
        "Note": Notebook("Note", "None", 0, 1),
        "HZ_c-I": Notebook("HZ_c-I", "None", 100, 5)
    }

    listNotes = ["Note", "HZ_c-I"]

