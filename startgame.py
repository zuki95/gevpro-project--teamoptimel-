#!/usr/bin/python3

from PyQt4 import QtGui, QtCore
import sys
import play
import playerAction
from play import *
from playerAction import *


class Start(QtGui.QWidget):
	def __init__(self):
		super(Start, self).__init__()
		self.initUI()
		
	def initUI(self):
	
		self.setWindowTitle("BATTLESHIP by TeamOptimel")
		self.setGeometry(0, 0, 400, 400)
		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)
	
		self.startButton = QtGui.QPushButton("Play Game!", self)
		self.name = QtGui.QLabel("TeamOptimel 2015")
	
		self.grid.addWidget(self.startButton, 1, 0)
		self.grid.addWidget(self.name, 2, 0)
	
		self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
		self.show()
	
		self.startButton.clicked.connect(self.startgame)
	
	def startgame(self):
		self.close()
		
		play.GridView()
		
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	startgame = Start()
	startgame.show()
	app.exec_()
		

	
