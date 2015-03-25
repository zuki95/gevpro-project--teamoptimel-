#!/usr/bin/env python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from playerAction import *
from collections import namedtuple

class GridView(QWidget):

    def __init__(self):
        super(GridView,self).__init__()
        self.player = player1
        player1.buildPlayerGrids()
        player2.buildPlayerGrids()
        self.buildUI()
        
    def buildUI(self):

        self.mainLayout = QGridLayout()
        self.mainLayout.setSpacing(5)
        self.fireBtn = QPushButton("Fire!")
        
        self.mainLayout.addLayout(self.player.enemyLayout, 0, 0)
        self.mainLayout.addLayout(self.player.ownLayout, 0, 1)
        self.mainLayout.addWidget(self.fireBtn, 2, 0)
        self.setLayout(self.mainLayout)
    
    def popupWindow(self):
        popupWin = QMessageBox(self)
        popupWin.setWindowTitle("Change players")
        popupWin.setText("Your turn is over. MOVE YOUR FUCKING ASS BRAH!")
        popupWin.exec()
        #self.player.enemyLayoutParent.hide()
        #self.player.enemyLayoutParent.show()
        #print(self.player.enemyLayout.parentWidget())
        self.changeTurns()
        self.buildUI()

        mainLayout = QGridLayout()
        mainLayout.setSpacing(5)
        self.enemyLayout = QGridLayout()
        self.enemyLayout.setSpacing(0)
        self.ownLayout = QGridLayout()
        self.ownLayout.setSpacing(0)
        self.buildGrids()
        
        # Build main grid
        fireBtn = QPushButton("Fire!")
        placeShip = QPushButton("Place Ship")
        placeShip.clicked.connect(lambda: self.placeShip())
        directionBtn = QPushButton("Horizontal", self)
        directionBtn.clicked.connect(lambda: self.direction())
        
        mainLayout.addLayout(self.enemyLayout, 0, 0)
        mainLayout.addLayout(self.ownLayout, 0, 1)
        mainLayout.addWidget(fireBtn, 2, 0)

        mainLayout.addWidget(placeShip, 4, 0)
        mainLayout.addWidget(directionBtn, 5, 0)
        
        self.setWindowTitle("Battleships")
        #self.setGeometry(300, 300, 800, 300)
        self.setLayout(mainLayout)
        
        
    def buildGrids(self):
        # Build the enemy grid
        for i, item in enumerate(self.player.enemyGrid):
            itemStr = str(item[1])
            xCoord = item[0][0]
            yCoord = item[0][1]
            row, col = divmod(i, 10)
            if (itemStr == "0"):
                itemLabel = QPushButton(str(col) + str(row), self)
                itemLabel.clicked.connect(lambda: self.prepareMissile())
            elif (itemStr == "1"):
                itemLabel = QLabel("-")
            else:
                itemLabel = QLabel(itemStr)
            
            itemLabel.setMaximumWidth(40)
            itemLabel.setStyleSheet("border: 1px solid #000;")
         
            self.enemyLayout.addWidget(itemLabel, yCoord, xCoord)
        
        # Build the own grid
        for y in range(10):
            for x in range(10):
                for item in self.player.shipCoords:
                    if ((item.x == x) and (item.y == y)):
                        shipLabel = QLabel(item.letter)
                    else:
                        shipLabel = QLabel(" ")
                    
                    shipLabel.setStyleSheet("border: 1px solid darkgrey;")
                    self.ownLayout.addWidget(shipLabel, y, x)

    def rebuildUI(self, sender, coordTuple, result):
        #self.enemyLayout.removeWidget(self.enemyLayout.itemAtPosition(coordTuple[0], coordTuple[1]))
        #self.enemyLayout.removeWidget(self.enemyLayout.itemAtPosition(coordTuple[0], coordTuple[1]))
        self.enemyLayout.removeWidget(sender)
        sender.deleteLater()
        #print(sender)
        #print(cItem)
        cItem = QLabel(str(result))
        self.enemyLayout.addWidget(cItem, coordTuple[1], coordTuple[0])
        #print(cItem)
    
    def placeShip(self):
        print("Hey")
        
    def direction(self):
        if self.directionBtn.text() == "Horizontal":
            self.directionBtn.setText("Vertical")
        else:
            self.directionBtn.setText("Horizontal")
		
        
    def prepareMissile(self):
        sender = self.sender()
        sendTuple = tuple(sender.text())
        sendSum = int(sendTuple[0]) + int(sendTuple[1])
        sendTuple = tuple((int(sendTuple[0]), int(sendTuple[1])))
        print(sendTuple)
        
    def changeTurns(self):
        if (self.player == player1):
            self.player = player2
        else:
            self.player = player1
        print('switch')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player1 = NewPlayer("johan")
    player2 = NewPlayer("nietjohan")
    
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
    player1.placeShips(shipList)
    player2.placeShips(shipList)
    
    
    board = GridView()
    board.show()
    player1.board = board
    player2.board = board
    app.exec()
    
    
    # Print een overzichtelijke enemyGrid
    gridList = ""
    for x in range(10):
        for y in range(10):
            number = (x * 10) + y
            gridList += str(player1.enemyGrid[number][1]) + " "
        
        gridList += "\n"
    
    print(gridList)
    
    # Print een overzichtelijke enemyGrid
    gridList = ""
    for x in range(10):
        for y in range(10):
            number = (x * 10) + y
            gridList += str(player2.enemyGrid[number][1]) + " "
        
        gridList += "\n"
    
    print(gridList)

    
    
