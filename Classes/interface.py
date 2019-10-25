import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


class MainWidgets(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Files/Interface.ui', self)
        # self.plankalkul_button.setGeometry(500, 0, 500, 150)
        # self.Open_upgrade_menu()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidgets()
    ex.show()
    sys.exit(app.exec_())
