from __future__ import absolute_import

from .Notebooks import NotesList
from .Soft import ProgrammsList
from .Languages import LanguagesList
import json



class Player:
    def __init__(self):
        # Инициализирую словарь. Будет использоваться для сохранения в json;
        self.stats = {"money": 10000000, "languages": ["Unknown", 0], "soft": ["notepad"], "notebook": "Note"}
        
        # Функция обновления характеристик;
        self.UpdateStats()
    

    # Сохранение;
    def Save(self):
        # Открываю файл;
        with open("Saves\\savePlayer.save", "w") as file:
            # Сериализую данные в json;
            json.dump(self.stats, file)
    
    # Загрузка;
    def Load(self):
        # Открываю файл;
        with open("Saves\\savePlayer.save", "r") as file:
            # Сериализую данные в json;
            self.stats = json.loads(file.read())
        # Обновление характеристик;
        self.UpdateStats()


    # Обновление характеристик;
    def UpdateStats(self):
        # Получаю ноутбук;
        self.notebook = NotesList.dictionaryNotes[self.stats["notebook"]]
        # Получаю установленный софт;
        self.soft = ProgrammsList.dictionarySoft[self.stats["soft"][0]]
        # Получаю прокачку языка;
        self.language = LanguagesList.dictionaryLanguages[self.stats["languages"][0]]

        # Суммирую урон;
        self.damage = self.notebook.damage + self.soft.damage + self.language.levelsKnow[self.stats["languages"][1]]["damage"]


    # Покупка ноутбука;
    def BuyNewNotebook(self):
        # Получаю номер текущего ноутбука;
        num = NotesList.listNotes.index(self.stats["notebook"])

        # Смотрю не последний ли это доступный ноутбук;
        if (num + 1 < len(NotesList.listNotes)):
            # Смотрю достаточно ли денег;
            if (self.stats["money"] - NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].price >= 0):
                # Обновляю словарь;
                self.stats["notebook"] = NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].name
                # Списываю деньги;
                self.stats["money"] -= NotesList.dictionaryNotes[NotesList.listNotes[num + 1]].price
                # Обновляю характеристики;
                self.UpdateStats()
    

    # Покупка новой программы;
    def BuySoft(self):
        # Получаю номер текущего программы;
        num = ProgrammsList.listSoft.index(self.stats["soft"][0])

        # Смотрю не последний ли это доступная программа;
        if (num + 1 < len(ProgrammsList.listSoft)):
            # Смотрю достаточно ли денег;
            if (self.stats["money"] - ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num + 1]].price >= 0):
                # Обновляю словарь;
                self.stats["soft"] = [ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num + 1]].name]
                # Списываю деньги;
                self.stats["money"] -= ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num + 1]].price
                # Обновляю характеристики;
                self.UpdateStats()


    # Улучшение уровня владения Языком программирования;
    def UpdateLevelLanguage(self):
        # Смотрю не последний ли это доступный уровень прокачки;
        if (self.stats["languages"][1] + 1 < len(LanguagesList.dictionaryLanguages[self.stats["languages"][0]].levelsKnow.keys())):
            # Смотрю достаточно ли денег;
            if (self.stats["money"] - LanguagesList.dictionaryLanguages[self.stats["languages"][0]].levelsKnow[self.stats["languages"][1] + 1]["price"] >= 0):
                # Списываю деньги;   
                self.stats["money"] -= LanguagesList.dictionaryLanguages[self.stats["languages"][0]].levelsKnow[self.stats["languages"][1] + 1]["price"]
                # Обновляю словарь;
                self.stats["languages"][1] += 1
                # Обновляю характеристики;
                self.UpdateStats()
        else:
            # Смотрю не последний ли это Язык программирования;
            if (LanguagesList.listLanguages.index(self.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
                # Смотрю достаточно ли денег;
                if (self.stats["money"] - LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(self.stats["languages"][0]) + 1]].levelsKnow[0]["price"] >= 0):
                    # Списываю деньги;   
                    self.stats["money"] -= LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(self.stats["languages"][0]) + 1]].levelsKnow[0]["price"]
                    # Обновляю словарь;
                    self.stats["languages"][0] = LanguagesList.listLanguages[LanguagesList.listLanguages.index(self.stats["languages"][0]) + 1]
                    self.stats["languages"][1] = 0
                    # Обновляю характеристики;
                    self.UpdateStats()



