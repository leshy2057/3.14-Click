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
        "Plankalkul": Language("Plankalkul", {
            0: {"damage": 1, "price": 0},
            1: {"damage": 5, "price": 100},
            2: {"damage": 10, "price": 200},
            3: {"damage": 15, "price": 300},
        }),
        "Fortran": Language("Fortran", {
            0: {"damage": 16, "price": 1000},
            1: {"damage": 17, "price": 1200},
            2: {"damage": 19, "price": 1500},
            3: {"damage": 25, "price": 2000},
            4: {"damage": 30, "price": 3000},
            5: {"damage": 32, "price": 5000},
        }),
        "Ada": Language("Ada", {
            0: {"damage": 32, "price": 10000},
            1: {"damage": 34, "price": 12000},
        }),
        "Basic": Language("Basic", {
            0: {"damage": 37, "price": 14000},
            1: {"damage": 40, "price": 17000},
        }),
        "Pascal": Language("Pascal", {
            0: {"damage": 45, "price": 20000},
            1: {"damage": 49, "price": 23000},
            2: {"damage": 52, "price": 24000},
            3: {"damage": 60, "price": 25000},
            4: {"damage": 61, "price": 24000},
        }),
        "C++": Language("C++", {
            0: {"damage": 65, "price": 30000},
            1: {"damage": 69, "price": 33000},
            2: {"damage": 73, "price": 37000},
            3: {"damage": 77, "price": 41000},
            4: {"damage": 81, "price": 45000},
        }),
        "Python": Language("Python", {
            0: {"damage": 90, "price": 55000},
            1: {"damage": 99, "price": 65000},
            2: {"damage": 108, "price": 75000},
            3: {"damage": 117, "price": 85000},
            4: {"damage": 126, "price": 95000},
        }),
        "Java": Language("Java", {
            0: {"damage": 140, "price": 110000},
            1: {"damage": 155, "price": 125000},
            2: {"damage": 170, "price": 140000},
            3: {"damage": 185, "price": 155000},
            4: {"damage": 200, "price": 170000},
        }),
        "Php": Language("Php", {
            0: {"damage": 250, "price": 220000},
            1: {"damage": 300, "price": 300000},
            2: {"damage": 400, "price": 420000},
            3: {"damage": 600, "price": 500000},
            4: {"damage": 900, "price": 800000},
        }),
        "C#": Language("C#", {
            0: {"damage": 1500, "price": 1500000},
            1: {"damage": 2000, "price": 2000000},
            2: {"damage": 3000, "price": 3000000},
            3: {"damage": 5000, "price": 5000000},
            4: {"damage": 10000, "price": 10000000},
        }),
        "Python 4.0": Language("Python 4.0", {
            0: {"damage": 100000, "price": 15000000},
            1: {"damage": 200000, "price": 20000000},
            2: {"damage": 300000, "price": 30000000},
            3: {"damage": 500000, "price": 50000000},
            4: {"damage": 1000000, "price": 100000000},
        }),
    }

    # Список всех языков;
    listLanguages = ["Plankalkul", "Fortran", "Ada", "Basic", "Pascal", "C++", "Python", "Java", "Php", "C#", "Python 4.0"]
    pictures_dict = {
        'Plankalkul': 'Images/languages/ada.jpg',
        'Fortran': 'Images/languages/fortran.jpg', 
        'Ada':'Images/languages/ada.jpg', 
        'Basic':'Images/languages/basic.jpg',
        'Pascal': 'Images/languages/pascal.jpg', 
        'C++': 'Images/languages/c++.png',
        'Python': 'Images/languages/python.jpg',
        'Java': 'Images/languages/java.png',
        'Php': 'Images/languages/php.png',
        'C#': 'Images/languages/c#.png',
        'Python 4.0': 'Images/languages/python.jpg'
    }
