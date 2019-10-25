# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'none.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UpdateWidget(QtWidgets.QWidget):
    def setupUi(self, Form):
        self.setObjectName("Form")
        self.resize(501, 141)
        self.setStyleSheet("background-image: url(D:\\GITHUB\\3.14-Click\\Images\\button.jpg);")
        self.SHOP = QtWidgets.QPushButton(Form)
        self.SHOP.setGeometry(QtCore.QRect(340, 0, 161, 61))
        self.SHOP.setObjectName("SHOP")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setGeometry(QtCore.QRect(0, 0, 141, 141))
        self.Image.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(140, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Level = QtWidgets.QLabel(Form)
        self.Level.setGeometry(QtCore.QRect(450, 80, 41, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Level.setFont(font)
        self.Level.setObjectName("Level")
        self.Damage = QtWidgets.QLabel(Form)
        self.Damage.setGeometry(QtCore.QRect(340, 80, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Damage.setFont(font)
        self.Damage.setObjectName("Damage")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(146, 82, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SHOP.setText(_translate("Form", "SHOP"))
        self.Name.setText(_translate("Form", "NAME"))
        self.Level.setText(_translate("Form", "LEVEL"))
        self.Damage.setText(_translate("Form", "DAMAGE"))
        self.label.setText(_translate("Form", "MONEY"))
