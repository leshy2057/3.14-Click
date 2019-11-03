# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import threading, time
from .Item import Item
from .Enemy import Enemy
from random import randint
from PyQt5.QtGui import QPixmap
from .Notebooks import NotesList


def thread(func):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.start()
        return wrapper



class Interface(QtWidgets.QMainWindow):
    def __init__(self, player):
        super().__init__()

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(30)
        
        self.player = player
        self.enemy = Enemy(player)

        # создание окна
        self.setObjectName("MainWindow")
        self.setGeometry(300, 300, 500, 800)

        # создание кнопочек
        self.soft_button = QtWidgets.QPushButton(self)
        self.soft_button.setGeometry(QtCore.QRect(10, 0, 150, 100))
        self.soft_button.setStyleSheet("background-image: url(Images/Programms.jpg);")
        self.soft_button.setText("")
        self.soft_button.setObjectName("soft_button")

        self.language_button = QtWidgets.QPushButton(self)
        self.language_button.setGeometry(QtCore.QRect(175, 0, 150, 100))
        self.language_button.setStyleSheet("background-image: url(Images/Language.jpg);")
        self.language_button.setText("")
        self.language_button.setObjectName("language_button")

        self.pc_button = QtWidgets.QPushButton(self)
        self.pc_button.setGeometry(QtCore.QRect(340, 0, 150, 100))
        self.pc_button.setStyleSheet("background-image: url(Images/Leptops.jpg);")
        self.pc_button.setText("")
        self.pc_button.setObjectName("pc_button")
    
        self.money = QtWidgets.QLabel(self)
        self.money.move(0, 731)
        self.money.resize(500, 39)
        self.money.setStyleSheet("color: rgb(200, 200, 0);")
        self.money.setText(str(self.player.stats["money"]))
        fontH = QtGui.QFont()
        fontH.setFamily("HACKED")
        fontH.setPointSize(20)
        self.money.setFont(fontH)
        self.money.setObjectName("money")
        self.money.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.money.setStyleSheet("#money {background-image: url(Images/MoneyImage.png);}")

        self.bug_widget = QtWidgets.QPushButton(self)
        self.bug_widget.move(0, 0)
        self.bug_widget.resize(500, 600)
        self.bug_widget.setFlat(True)
        self.bug_widget.setObjectName("bug_widget")
        self.bug_widget.clicked.connect(lambda: (self.AnimaBugClick(False), self.enemy.AddDamage(), self.BugClick()))
        self.bug_widget.setStyleSheet("""
        QPushButton:focus {
    	    border: none;
    	    outline: none;
        }""")
        self.bug_widget.setIconSize(QtCore.QSize(251, 251))

        self.healthBar = QtWidgets.QFrame(self)
        self.healthBar.setGeometry(QtCore.QRect(0, 770, 500, 30))
        self.healthBar.setObjectName("healthBar")
        self.healthBar.setStyleSheet("#healthBar {background-image: url(Images/HealtBar1.png);}")

        self.soft_button.raise_()
        self.language_button.raise_()
        self.pc_button.raise_()

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.soft_button.clicked.connect(lambda: self.SetClicks("soft"))
        self.pc_button.clicked.connect(lambda: self.SetClicks("notes"))
        self.language_button.clicked.connect(lambda: self.SetClicks("languages"))

        self.boss_warning = QtWidgets.QLabel(self) 
        self.boss_warning.move(500,150)
        self.boss_warning.setStyleSheet("color: rgb(200, 10, 0);")
        self.boss_warning.setText('BOSS')
        self.boss_warning.setFont(font)

        self.widget = QtWidgets.QLabel(self)
        self.widget.move(140, 410)
        self.widget.resize(300, 300)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.widget.setPixmap(QtGui.QPixmap("Images/pc/0pc.png);"))

        self.GetBugImage()

        self.setStyleSheet("#MainWindow {background-image: url(Images/fon.png);}")

        self.hideItem = False
        self.lastItem = ""
        self.widget.raise_()
        self.item = Item(self)
        self.OffItem()
        self.update()
        self.UpdateNote(player)
        self.startAudio()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3.14-Click"))
    
    def startAudio(self):
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("Files\\Sound\\MainTheme.mp3")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)

        self.sound = QtMultimedia.QSound("Files\\Sound\\ClickSound.wav")

        self.audio = QtMultimedia.QMediaPlayer()
        self.audio.setPlaylist(self.playlist)
        self.audio.play()
        self.audio.setVolume(20)
        

    def GetBugImage(self):
        if self.enemy.boss == 1:
            self.boss_warning.move(500, 150)
            bug ='Images/bugs/bug' + str(randint(1, 6)) + '.png'
            self.bug_widget.setIcon(QtGui.QIcon(QtGui.QPixmap(bug)))
            self.enemy.SetImage(bug)
        elif self.enemy.boss == 5:
            self.boss_warning.move(200, 150)
            bug ='Images/bugs/bugboss' + str(randint(1, 3)) + '.png'
            self.enemy.SetImage(bug)
            self.bug_widget.setIcon(QtGui.QIcon(QtGui.QPixmap(bug)))

    def UpdateNote(self, player):
        self.widget.setStyleSheet(f"#widget {{background-image: url({NotesList.dictNotes[player.stats['notebook']]});}}")

    def GetNote(self, player):
        num = NotesList.listNotes.index(player.stats["notebook"])

        if (num + 1 < len(NotesList.listNotes)):
            return NotesList.dictionaryNotes[NotesList.listNotes[num + 1]]
        else:
            return NotesList.dictionaryNotes[NotesList.listNotes[num]]

    def closeEvent(self, event):
        self.Save()

    def Save(self):
        self.player.Save()
        self.enemy.Save()
    
    def Load(self):
        self.player.Load()
        self.money.setText(str(self.player.stats["money"]))

        self.enemy.Load(self.player)
        if (self.enemy.stats["image"] != "None"):
            self.bug_widget.setIcon(QtGui.QIcon(QtGui.QPixmap(self.enemy.stats["image"])))
        else:
            self.GetBugImage()

        if self.enemy.boss == 5:
            self.boss_warning.move(200, 150)
        
        self.healthBar.resize(5 * self.enemy.GetDamageForUI(), self.healthBar.size().height())
        self.UpdateNote(self.player)

    @thread
    def AnimaBugClick(self, none):
        self.bug_widget.setIconSize(QtCore.QSize(228, 228))
        time.sleep(0.1)
        self.bug_widget.setIconSize(QtCore.QSize(251, 251))
        return

    # Событие клика по жуку;
    def BugClick(self):
        self.sound.play()
        # Если враг побуждён:
        if (self.enemy.dead):
            # Создаю нового врага;
            self.enemy = Enemy(self.player)
            self.GetBugImage()
        # Обновляю размер helthBar'a;
        self.healthBar.resize(5 * self.enemy.GetDamageForUI(), self.healthBar.size().height())
        # Обновляю текст монеток;
        self.money.setText(str(self.player.stats["money"]))
        # Скрываю окно обновлений;
        self.OffItem()
        self.UpdateNote(self.player)

    # Если нажата одна из кнопок улучшения;
    def SetClicks(self, getType):
        if (self.hideItem and getType == self.lastItem):
            # Скрываю окно обновлений;
            self.OffItem()
        else:
            # Показываю окно обновлений;
            self.OnItem()
            # Настраиваю Item;
            self.item.Setting(self.player, getType, func=self.UpdateNote, money=self.money)
        self.lastItem = getType
        self.update()
    
    def OnItem(self):
        self.hideItem = True
        self.item.setVisible(True)
        self.item.backgound.setVisible(True)
    
    def OffItem(self):
        self.hideItem = False
        self.item.setVisible(False)
        self.item.backgound.setVisible(False)
