# Класс языка;
class Language:
    def __init__(self, getName, getLevelsKnow):
        # Имя;
        self.name = getName
        # Возможные уровни знания языка;
        self.levelsKnow = getLevelsKnow



# Класс содержащий в себе все Языки программирования;
class LanguagesList:
    # Собственно словарь в котором всё храниться;
    dictionaryLanguages = {
        # "<Имя языка>": Language("<Имя>", { <Уровень знания>: {"damage": <Урон на данном уровне>, "price": <Цена перехода на этот уровнь>} })
        "Unknown": Language("Unknown", {
            0: {"damage": 1, "price": 0},
            1: {"damage": 5, "price": 100},
            2: {"damage": 10, "price": 200},
            3: {"damage": 15, "price": 300},
        }),
        "Fortan": Language("Fortan", {
            0: {"damage": 15, "price": 1000},
            1: {"damage": 17, "price": 1200},
            2: {"damage": 19, "price": 1500},
            3: {"damage": 25, "price": 2000},
            4: {"damage": 30, "price": 3000},
            5: {"damage": 32, "price": 5000},
        }),
        "Ада": Language("Ада", {
            0: {"damage": 32, "price": 10000},
            1: {"damage": 45, "price": 12000},
        }),
        "Objective-C": Language("Objective-C", {
            0: {"damage": 45, "price": 20000},
            1: {"damage": 49, "price": 23000},
            2: {"damage": 52, "price": 24000},
            3: {"damage": 60, "price": 25000},
            4: {"damage": 61, "price": 24000},
        }),
    }

    # Список всех языков;
    listLanguages = ["Unknown", "Fortan", "Ада", "Objective-C"]

