#!/usr/bin/env python
#Kamil

from PyQt4 import QtGui, QtCore
import os, sys
import playerAction
import gui



class Start(QtGui.QWidget):
	def __init__(self):
		super(Start, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle("BattleShips")
		self.setGeometry(0, 0, 300, 300)
		
		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)
		
		self.btn = QtGui.QPushButton("Start Game", self)
		
		
		self.names = QtGui.QLabel("© 2015 Team Optimel.")
		self.grid.addWidget(self.btn, 1, 0)
		
		self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
		self.show()
		
		self.btn.clicked.connect(self.startGame)
		
	def startGame(self):
		self.close()
		
		#Go to game, nog nie
		gui.GridView()
		
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	f = Start()
	f.show()
	app.exec_()
		
		
