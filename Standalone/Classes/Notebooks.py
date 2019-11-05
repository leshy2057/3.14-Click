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
        # "Имя ноутбука": Notebook("<Имя>", "<Описание>", <Цена>, <Урон>);
        "Note": Notebook("Note", "None", 0, 1),
        "HZ_c-I": Notebook("HZ_c-I", "None", 100, 5),
        "HZ_c-II": Notebook("HZ_c-II", "None", 1000, 10),
        "HZ_c-III": Notebook("HZ_c-III", "None", 2000, 15),
        "Lenovo-2001": Notebook("Lenovo-2001", "None", 5000, 35),
        "MSI-318": Notebook("MSI-318", "None", 15000, 130),
        "MacBook": Notebook("MacBook", "None", 50000, 400),
        "NYTRO-2077": Notebook("NYTRO-2077", "None", 200000, 2000),
        "PC for school": Notebook("PC for school", "None", 1000000, 9999),
    }

    # Список всех ноутбуков;
    listNotes = ["Note", "HZ_c-I", "HZ_c-II", "HZ_c-III", "Lenovo-2001", 
    "MSI-318", "MacBook", "NYTRO-2077", "PC for school"]

    dictNotes = {
        "Note": 'Images/pc/0pc.png',
        "HZ_c-I": 'Images/pc/1pc.png',
        "HZ_c-II": 'Images/pc/2pc.png',
        "HZ_c-III": 'Images/pc/3pc.png',
        "Lenovo-2001": 'Images/pc/4pc.png',
        "MSI-318": 'Images/pc/5pc.png',
        "MacBook": 'Images/pc/6pc.png',
        "NYTRO-2077": 'Images/pc/7pc.png',
        "PC for school": 'Images/pc/8pc.png',
    }

