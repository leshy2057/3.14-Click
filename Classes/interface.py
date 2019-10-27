# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading, time
from .Item import Item
from .Enemy import Enemy


def thread(func):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.start()
        return wrapper



class Interface(QtWidgets.QMainWindow):
    def __init__(self, player):
        super().__init__()
        
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

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(30)

        self.health = QtWidgets.QLabel(self)
        self.health.move(200, 750)
        self.health.setStyleSheet("color: rgb(200, 10, 0);")
        self.health.setText(str(self.enemy.GetDamageForUI()))
        self.health.setFont(font)

        self.money = QtWidgets.QLabel(self)
        self.money.move(0, 750)
        self.money.resize(200, 25)
        self.money.setStyleSheet("color: rgb(200, 200, 0);")
        self.money.setText(str(self.player.stats["money"]))
        self.money.setFont(font)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(140, 410, 300, 300))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-image: url(Images/Notes/1pc.png);")
        self.widget.setObjectName("widget")

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
        self.bug_widget.setIcon(QtGui.QIcon(QtGui.QPixmap("Images/жуг.png")))
        self.bug_widget.setIconSize(QtCore.QSize(251, 251))

        self.widget.raise_()
        self.soft_button.raise_()
        self.language_button.raise_()
        self.pc_button.raise_()
        # self.bug_widget.raise_()

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
        self.pc_button.clicked.connect(lambda: self.SetClicks("pc"))
        self.language_button.clicked.connect(lambda: self.SetClicks("language"))

        # self.shopEverything = Item(self)
        # self.shopEverything.raise_()

        self.setStyleSheet("background-image: url(Images/fon.png);")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3.14-Click"))

    @thread
    def AnimaBugClick(self, none):
        self.bug_widget.setIconSize(QtCore.QSize(228, 228))
        time.sleep(0.1)
        self.bug_widget.setIconSize(QtCore.QSize(251, 251))

    # Событие клика по жуку;
    def BugClick(self):
        # Если враг побуждён:
        if (self.enemy.dead):
            # Создаю нового врага;
            self.enemy = Enemy(self.player)
        # Обновляю текст здоровья;
        self.health.setText(str(self.enemy.GetDamageForUI()))
        # Обновляю текст монеток;
        self.money.setText(str(self.player.stats["money"]))

    def SetClicks(self, getType):
        pass
        #self.shopEverything.Setting(self.player, getType)
