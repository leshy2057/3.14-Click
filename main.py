import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Classes.Item import Item
from Classes.Player import Player
from Classes.interface import Interface

 
class MyWidget(Interface):
    def __init__(self):
        self.player = Player()
        super().__init__(self.player)
        self.update()
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

