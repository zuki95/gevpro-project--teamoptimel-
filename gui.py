#!/usr/bin/env python
#Kamil Zukowski

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from playerAction import *
from collections import namedtuple

class GridView(QWidget):

    def __init__(self):
        super(GridView,self).__init__()
        
        self.buildUI()
        
    def buildUI(self):
        mainLayout = QGridLayout()
        mainLayout.setSpacing(5)
        self.enemyLayout = QGridLayout()
        self.enemyLayout.setSpacing(0)
        self.ownLayout = QGridLayout()
        self.ownLayout.setSpacing(0)
        
        self.buildGrids()
        
        # Build main grid
        fireBtn = QPushButton("Fire!")
        
        mainLayout.addLayout(self.enemyLayout, 0, 0)
        mainLayout.addLayout(self.ownLayout, 1, 0)
        mainLayout.addWidget(fireBtn, 2, 0)
        

        self.setLayout(mainLayout)
        
    def buildGrids(self):
        # Build the enemy grid
        for i, item in enumerate(player.enemyGrid):
            itemStr = str(item[1])
            xCoord = item[0][0]
            yCoord = item[0][1]
            row, col = divmod(i, 10)
            if (itemStr == "0"):
                itemLabel = QPushButton(str(col) + "," + str(row), self)
                itemLabel.clicked.connect(lambda: self.prepareMissile())
            elif (itemStr == "1"):
                itemLabel = QLabel("-")
            else:
                itemLabel = QLabel(itemStr)
            
            itemLabel.setMaximumWidth(40)
            itemLabel.setStyleSheet("border: 1px solid #000;")
         
            self.enemyLayout.addWidget(itemLabel, xCoord, yCoord)
        
        # Build the own grid
        for y in range(10):
            for x in range(10):
                for item in player.shipCoords:
                    if ((item.x == x) and (item.y == y)):
                        shipLabel = QLabel(item.letter)
                    else:
                        shipLabel = QLabel(" ")
                    
                    shipLabel.setStyleSheet("border: 1px solid darkgrey;")
                    self.ownLayout.addWidget(shipLabel, y, x)

    def prepareMissile(self):
        sender = self.sender()
        print(sender.text())

if __name__ == "__main__":
    player = NewPlayer("johan")
    
    BattleShip = namedtuple("BattleShip", "x, y, letter")
    shipList = []
    
    ship1 = BattleShip(1, 1, "L")
    ship2 = BattleShip(2, 1, "O")
    ship3 = BattleShip(3, 1, "L")
    ship4 = BattleShip(5, 1, "T")
    ship5 = BattleShip(6, 1, "H")
    ship6 = BattleShip(7, 1, "I")
    ship7 = BattleShip(8, 1, "S")
    ship8 = BattleShip(4, 4, "S")
    ship9 = BattleShip(5, 4, "U")
    ship10 = BattleShip(6, 4, "C")
    ship11 = BattleShip(7, 4, "K")
    ship12 = BattleShip(8, 4, "S")
    
    shipList.append(ship1)
    shipList.append(ship2)
    shipList.append(ship3)
    shipList.append(ship4)
    shipList.append(ship5)
    shipList.append(ship6)
    shipList.append(ship7)
    shipList.append(ship8)
    shipList.append(ship9)
    shipList.append(ship10)
    shipList.append(ship11)
    shipList.append(ship12)
    player.placeShips(shipList)
    
    print(shipList)
    
    """
    print(fireMissile(player, (1, 6)))
    print(fireMissile(player, (2, 6)))
    print(fireMissile(player, (3, 6)))
    print(fireMissile(player, (4, 6)))
    print(fireMissile(player, (4, 5)))
    print(fireMissile(player, (8, 2)))
    
    """
    app = QApplication(sys.argv)
    f = GridView()
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

    
    
