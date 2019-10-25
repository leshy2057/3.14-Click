# Класс программы;
class Programm:
    def __init__(self, getName, getPrice, getDamage):
        # Имя;
        self.name = getName
        # Урон;
        self.damage = getDamage

        # Цена;
        self.price = getPrice



# Класс содержащий в себе все программы;
class ProgrammsList:
    # Собственно словарь в котором всё храниться;
    dictionarySoft = {
        # "<Имя программы>": Programm("<Имя>", <Цена>, <Урон>);
        "notepad": Programm("notepad", 0, 1),
        "notepad-I": Programm("notepad-I", 100, 2),
        "notepad-II": Programm("notepad-II", 200, 4),
        "notepad-III": Programm("notepad-III", 500, 8),
        "notepad-IV": Programm("notepad-IV", 1000, 10),
        "notepad-V": Programm("notepad-V", 1500, 15),
    }

    # Список всех программ;
    listSoft = ["notepad", "notepad-I", "notepad-II", "notepad-III", "notepad-IV", "notepad-V"]




