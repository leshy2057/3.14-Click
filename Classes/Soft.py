class Programm:
    def __init__(self, getName, getPrice, getDamage):
        self.name = getName
        self.damage = getDamage

        self.price = getPrice



class ProgrammsList:
    dictionarySoft = {
        "notepad": Programm("Note", 0, 1),
    }

    listSoft = ["notepad"]




