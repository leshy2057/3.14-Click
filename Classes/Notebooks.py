# Класс ноутбука;
class Notebook:
    def __init__(self, getName, getDescription, getPrice, getDamage):
        # Имя;
        self.name = getName
        # Описание;
        self.description = getDescription
        # Цена;
        self.price = getPrice

        # Урон;
        self.damage = getDamage



# Класс содержащий в себе все ноутбуки;
class NotesList:
    # Собственно словарь в котором всё храниться;
    dictionaryNotes = {
        # "Имя ноутбука": Notebootk("<Имя>", "<Описание>", <Цена>, <Урон>);
        "Note": Notebook("Note", "None", 0, 1),
        "HZ_c-I": Notebook("HZ_c-I", "None", 100, 5),
        "HZ_c-II": Notebook("HZ_c-II", "None", 1000, 10),
        "HZ_c-III": Notebook("HZ_c-III", "None", 2000, 15),
    }

    # Список всех ноутбуков;
    listNotes = ["Note", "HZ_c-I", "HZ_c-II", "HZ_c-III"]

