class Language:
    def __init__(self, getName, getLevelsKnow):
        self.name = getName
        self.levelsKnow = getLevelsKnow



class LanguagesList:
    dictionaryLanguages = {
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
        }),
    }

    listLanguages = ["Unknown", "Fortan"]

