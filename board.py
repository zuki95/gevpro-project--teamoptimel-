#!/usr/bin/env python
#Kamil Zukowski

import sys
from PyQt4 import QtCore, QtGui

class Board(QtGui.QWidget):

    def __init__(self):
        super(Board,self).__init__()

        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.table = QtGui.QTableWidget(self)
        self.table.setRowCount(10)
        self.table.setColumnCount(10)
        grid.addWidget(self.table,1,0)
        self.setLayout(grid)
        self.setWindowTitle("Battleships")
        self.setGeometry(200,200,1100,350)
        self.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = Board()
    sys.exit(app.exec_())
    
