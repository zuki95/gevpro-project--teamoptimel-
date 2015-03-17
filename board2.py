#!/usr/bin/env python
#Kamil Zukowski

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from playerAction import *
from collections import namedtuple

class Board(QWidget):

    def __init__(self):
        super(Board,self).__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        for item in player.enemyGrid:
            itemStr = str(item[1])
            if (itemStr == "0"):
                itemLabel = QPushButton("Fire!")
                itemLabel.clicked.connect(lambda: fireMissile(player, item[0]))
            elif (itemStr == "1"):
                itemLabel = QLabel("-")
            else:
                itemLabel = QLabel(itemStr)
            
            itemLabel.setMaximumWidth(40)
            itemLabel.setStyleSheet("border: 2px solid #000;")
         
            grid.addWidget(itemLabel, item[0][0], item[0][1])
        
        #for item in player.shipCoords
        
        self.setLayout(grid)

if __name__ == "__main__":
    player = NewPlayer("johan")
    """
    BattleShip = namedtuple("BattleShip", "x, y, letter")
    shipList = []
    
    for i in range(3):
        myFirstRealShipOMG = BattleShip((2+i), 6, "L")
        shipList.append(myFirstRealShipOMG)
    player.placeShips(shipList)
    

    print(fireMissile(player, (1, 6)))
    print(fireMissile(player, (2, 6)))
    print(fireMissile(player, (3, 6)))
    print(fireMissile(player, (4, 6)))
    print(fireMissile(player, (4, 5)))
    print(fireMissile(player, (8, 2)))
    
    """
    app = QApplication(sys.argv)
    f = Board()
    f.show()
    app.exec()
    
    
    # Print een overzichtelijke enemyGrid
    gridList = ""
    for x in range(10):
        for y in range(10):
            number = (x * 10) + y
            gridList += str(player.enemyGrid[number][1]) + " "
        
        gridList += "\n"
    
    print(gridList)

    
    
