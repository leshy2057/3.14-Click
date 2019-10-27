from PyQt5 import QtCore, QtGui, QtWidgets
from Player import Player
from interface import Interface



class Bug:
    def __init__(self):
        self.bug_life = 100
        self.bug_life_count = self.bug_life
        self.UpdateStats()
    
    def BugLife(self):
        if Interface.sender() == Interface.bug_widget:
            self.bug_life_count -= self.damage
        if self.bug_life_count <= 0:
            self.UpdateBug(self.bug_life)

    def UpdateBug(self, bug_life):
        self.bug_life = self.bug_life * 1.2
    
    def UpdateStats(self):
        self.damage = Player.GiveDamage()
    
    def GiveBugLife(self):
        return bug_life, bug_life_count
    

    



