# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Item.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from .Notebooks import NotesList
from .Soft import ProgrammsList
from .Languages import LanguagesList



class Item(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        self.move(0, 0)
        self.resize(600, 200)
        self.backgound = QtWidgets.QFrame(Form)
        self.backgound.setGeometry(QtCore.QRect(0, 0, 601, 201))
        self.backgound.setStyleSheet("background-color: rgb(239, 241, 222);")
        self.backgound.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgound.setObjectName("backgound")
        self.image = QtWidgets.QLabel(self.backgound)
        self.image.setGeometry(QtCore.QRect(0, 0, 201, 201))
        self.image.setStyleSheet("background-image: url(Images/Notes/1pc.png) 0 0 0 0 stretch stretch; border-width: 0px;") # background-color: rgb(255, 0, 0);
        self.image.setText("")
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.backgound)
        self.label.setGeometry(QtCore.QRect(200, 60, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(144, 142, 134);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.backgound)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(144, 142, 134);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.backgound)
        self.label_3.setGeometry(QtCore.QRect(200, 0, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(144, 142, 134);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.backgound)
        self.label_4.setGeometry(QtCore.QRect(200, 150, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(144, 142, 134);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.backgound)
        self.pushButton.setGeometry(QtCore.QRect(490, 150, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(144, 142, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Damage"))
        self.label_2.setText(_translate("Form", "Level"))
        self.label_3.setText(_translate("Form", "Name"))
        self.label_4.setText(_translate("Form", "Price"))
        self.pushButton.setText(_translate("Form", "Shop"))
    

    def settingText(self, player, getType):
        if getType == "languages":
            lang = self.GetLanguage(player)

            if (player.stats["languages"][1] + 1 < len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
                self.label_3.setText(lang.name) # Имя
                self.label_4.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["price"])) # Цена
                self.label_2.setText(f'N: {str(player.stats["languages"][1] + 1)}') # Уровень
                self.label.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["damage"])) # Урон
            elif (player.stats["languages"][1] + 1 == len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
                if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
                    lang = LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1]]
                    self.label_3.setText(lang.name) # Имя
                    self.label_4.setText(str(lang.levelsKnow[0]["price"])) # Цена
                    self.label_2.setText(str(1)) # Уровень
                    self.label.setText(str(lang.levelsKnow[0]["damage"])) # Урон
                else:
                    self.label_3.setText(LanguagesList.listLanguages[-1]) # Имя
                    self.label_4.setText("MAX") # Цена
                    self.label_2.setText("MAX") # Уровень
                    self.label.setText(str(lang.levelsKnow[player.stats["languages"][1]]["damage"])) # Урон
            else:
                self.label_3.setText(lang.name) # Имя
                self.label_4.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["price"])) # Цена
                self.label_2.setText(str(1)) # Уровень
                self.label.setText(str(lang.levelsKnow[player.stats["languages"][1]]["damage"])) # Урон
        if getType == "notes":
            note = self.GetNote(player)

            if (note.name != NotesList.listNotes[-1]):
                self.label_3.setText(note.name) # Имя
                self.label_4.setText(str(note.price)) # Цена
                self.label_2.setText('MAX') # Уровень
                self.label.setText(str(note.damage)) # Урон
            else:
                self.label_3.setText(note.name) # Имя
                self.label_4.setText('MAX') # Цена
                self.label_2.setText('MAX') # Уровень
                self.label.setText(str(note.damage)) # Урон
        if getType == "soft":
            soft = self.GetSoft(player)

            if (soft.name != player.stats["soft"]):
                self.label_3.setText(soft.name) # Имя
                self.label_4.setText(str(soft.price)) # Цена
                self.label_2.setText('MAX') # Уровень
                self.label.setText(str(soft.damage)) # Урон
            else:
                self.label_3.setText(soft.name) # Имя
                self.label_4.setText('MAX') # Цена
                self.label_2.setText('MAX') # Уровень
                self.label.setText(str(soft.damage)) # Урон


    def Setting(self, player, getType):
        self.pushButton.clicked.connect(lambda: self.UpdateSomeThing(player, getType))
        self.settingText(player, getType)

    def UpdateSomeThing(self, player, getType):
        if (getType == "languages"):
            player.UpdateLevelLanguage()
        elif (getType == "notes"):
            player.BuyNewNotebook()
        elif (getType == "soft"):
            player.BuySoft()
        self.settingText(player, getType)

    def GetLanguage(self, player):
        if (player.stats["languages"][1] + 1 <= len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
            return LanguagesList.dictionaryLanguages[player.stats["languages"][0]]
        if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
            if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
                return LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1]]
    
    def GetNote(self, player):
        num = NotesList.listNotes.index(player.stats["notebook"])

        if (num + 1 < len(NotesList.listNotes)):
            return NotesList.dictionaryNotes[NotesList.listNotes[num + 1]]
        else:
            return NotesList.dictionaryNotes[NotesList.listNotes[num]]
    
    def GetSoft(self, player):
        num = ProgrammsList.listSoft.index(player.stats["soft"])

        if (num + 1 < len(ProgrammsList.listSoft)):
            return ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num + 1]]
        else:
            return ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num]]
