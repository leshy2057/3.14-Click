# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        MainWindow.setStyleSheet("background-image: url(Images/fon.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.soft_button = QtWidgets.QPushButton(self.centralwidget)
        self.soft_button.setGeometry(QtCore.QRect(10, 0, 150, 100))
        self.soft_button.setStyleSheet("background-image: url(Images/Programms.jpg);")
        self.soft_button.setText("")
        self.soft_button.setObjectName("soft_button")
        self.language_button = QtWidgets.QPushButton(self.centralwidget)
        self.language_button.setGeometry(QtCore.QRect(175, 0, 150, 100))
        self.language_button.setStyleSheet("background-image: url(Images/Language.jpg);")
        self.language_button.setText("")
        self.language_button.setObjectName("language_button")
        self.pc_button = QtWidgets.QPushButton(self.centralwidget)
        self.pc_button.setGeometry(QtCore.QRect(340, 0, 150, 100))
        self.pc_button.setStyleSheet("background-image: url(Images/Leptops.jpg);")
        self.pc_button.setText("")
        self.pc_button.setObjectName("pc_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 410, 300, 300))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-image: url(Images/Notes/1pc.png);")
        self.widget.setObjectName("widget")
        self.bug_widget = QtWidgets.QWidget(self.centralwidget)
        self.bug_widget.setGeometry(QtCore.QRect(120, 159, 251, 251))
        self.bug_widget.setStyleSheet("background-image: url(Images/жуг.png);")
        self.bug_widget.setObjectName("bug_widget")
        self.widget.raise_()
        self.soft_button.raise_()
        self.language_button.raise_()
        self.pc_button.raise_()
        self.bug_widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3.14-Click"))

import files_rc
