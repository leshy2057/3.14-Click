# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Item.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 200)
        self.backgound = QtWidgets.QFrame(Form)
        self.backgound.setGeometry(QtCore.QRect(0, 0, 601, 201))
        self.backgound.setStyleSheet("background-color: rgb(239, 241, 222);")
        self.backgound.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgound.setObjectName("backgound")
        self.image = QtWidgets.QLabel(self.backgound)
        self.image.setGeometry(QtCore.QRect(0, 0, 201, 201))
        self.image.setStyleSheet("background-color: rgb(255, 0, 0);")
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
