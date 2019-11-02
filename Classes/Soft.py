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
        "cmd": Programm("cmd", 1000, 20),
        "IDE": Programm("IDE", 20000, 400),
        "Wing": Programm("Wing", 500000, 8000),
        "PyCharm": Programm("PyCharm", 1000000, 10000),
        "VSC": Programm("VSC", 2000000, 2000000),
    }

    # Список всех программ;
    listSoft = ["notepad", "cmd", "IDE", "Wing", "PyCharm", "VSC"]




