#!/usr/bin/env python

#########################################################################
#   This Battleships game is programmed by:                             #
#   Leon Graumans       l.graumans@student.rug.nl                       #
#   Johan Groenewold    j.groenewold.1@student.rug.nl                   #
#   Kamil Zukowski      k.zukowski@student.rug.nl                       #
#                                                                       #
#   This program is released under the                                  #
#   Creative Commons Attribution-NonCommercial 4.0 International        #
#   license, which means everyone is allowed to copy, share, edit and   #
#   adapt the code in any way they like, except for commercial use.     #
#   For more information, please check:                                 #
#   https://creativecommons.org/licenses/by-nc/4.0/                     #
#                                                                       #
#   Please note:                                                        #
#   This game requires the corresponding playerAction.py file and       #
#   PyQt version 4 or higher: http://pyqt.sourceforge.net/              #
#########################################################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from playerAction import *
from collections import namedtuple
from random import randrange, getrandbits

class ComputerPlayer:
    def __init__(self, name, level):
        """
        Class om een computerspeler aan te maken. Aan te roepen via
        nieuwe_speler = ComputerPlayer("gebruikersnaam", int)
        ,int 1-3 voor de moeilijkheidsgraad
        """
        self.name = name
        self.level = level
        self.shipCoords = []
        self.enemyGrid = []

        self.placeShips()


    def placeShips(self):
        """ Zet schepen op random plekken neer """
        for i in range(2, 5):
            for j in range(2):
                xCoord = randrange(0, 10)
                yCoord = randrange(0, 10)
                random = bool(getrandbits(1))
                """ random True/False for horizontal versus vertical placement """
                
                randWord = randomWord(i, 0)
                newShip = self.createShip(xCoord, yCoord, i, random, [])
                
                loopcount = 0
                withLetters = []
                for coord in newShip:
                    withLetters.append([coord, randWord[loopcount]])
                    loopcount += 1
                    
                    
                    
                if (newShip):
                    self.shipCoords.extend(withLetters)

    def createShip(self, xCoord, yCoord, shipSize, isHorizontal, shipCoordsList):
        """
        xCoord = yCoord are coordinates, shipSize is the size (2-4 blocks) of
        the ship, isHorizontal is randomly True/False for the orientation and
        the shipCoordsList is filled with coordinates.
        """

        if(len(shipCoordsList) == shipSize):
            return shipCoordsList

        if ((self.shipOnCoordinate((xCoord, yCoord))) or not ( 0 <= xCoord < 10) or not ( 0 <= yCoord < 10)):
            xCoord = randrange(0, 10)
            yCoord = randrange(0, 10)
            random = bool(getrandbits(1))
            return self.createShip(xCoord, yCoord, shipSize, random, [])
        shipCoordsList.append((xCoord, yCoord))

        if (isHorizontal):
            return self.createShip(xCoord+1, yCoord, shipSize, isHorizontal, shipCoordsList)
            return self.createShip(xCoord-1, yCoord, shipSize, isHorizontal, shipCoordsList)
        else:
            return self.createShip(xCoord, yCoord+1, shipSize, isHorizontal, shipCoordsList)
            return self.createShip(xCoord, yCoord-1, shipSize, isHorizontal, shipCoordsList)


    def shipOnCoordinate(self, coordTuple):
        """ checkt of er een schip is op de plek van het schot """
        for ship in self.shipCoords:
            if ((ship[0][0] == coordTuple[0]) and (ship[0][1] == coordTuple[1])):
                return ship[1]

        return 0

    def getCurrentEnemyGrid(self):
        return self.enemyGrid

    def updateEnemyGrid(self, coordTuple, result):
        """ update de enemyGrid met een nieuwe status """
        self.enemyGrid.append([coordTuple[0], coordTuple[1], result]    )


class TriggerPopup(QWidget):
    def __init__(self, title, text):
        super(TriggerPopup,self).__init__()
        #QWidget.__init__(self)
        
        popupLayout = QGridLayout()
        textLabel = QLabel(text)
        
        self.setWindowTitle(title)
        popupLayout.addWidget(textLabel)
        self.setLayout(popupLayout)


class GameView(QWidget):

    def __init__(self):
        super(GameView,self).__init__()
        
        self.buildUI()
        
    def buildUI(self):
        mainLayout = QGridLayout()
        mainLayout.setSpacing(5)
        self.enemyLayout = QGridLayout()
        self.enemyLayout.setSpacing(0)
        self.ownLayout = QGridLayout()
        self.ownLayout.setSpacing(0)
        self.labelList = []
        self.setWindowTitle("BATTLESHIP by TeamOptimel")
        
        self.buildGrids()
        
        """ Build main grid """
        self.statusBar = QLabel("Click somewhere on the right grid to fire")
        self.statusBar.setStyleSheet("font-size: 16px;")
        self.dictionary = QPushButton("Possible words", self)
        self.dictionary.clicked.connect(lambda: self.openWordList())
        yourGridLabel = QLabel("Your Grid")
        theirGridLabel = QLabel("Computer's Grid, drop them bombs here")
        
        layoutWrapper = QGridLayout()
        layoutWrapper.addWidget(yourGridLabel, 0, 0)
        layoutWrapper.addWidget(theirGridLabel, 0, 1)
        layoutWrapper.addLayout(self.enemyLayout, 1, 1)
        layoutWrapper.addLayout(self.ownLayout, 1, 0)
        mainLayout.addLayout(layoutWrapper, 0, 0)
        mainLayout.addWidget(self.statusBar, 1, 0)
        mainLayout.addWidget(self.dictionary, 2, 0)
        self.resize(800, 300)
        self.setLayout(mainLayout)
        
    def buildGrids(self):
        """ Build the enemy grid """
        for i, item in enumerate(player.enemyGrid):
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
        
        """ Build the own grid """
        for y in range(10):
            for x in range(10):
                for item in player.shipCoords:
                    if ((item.x == x) and (item.y == y)):
                        shipLabel = QLabel(item.letter)
                    else:
                        shipLabel = QLabel(" ")
                    
                    shipLabel.setStyleSheet("border: 1px solid darkgrey;")
                    self.ownLayout.addWidget(shipLabel, y, x)
                    
                self.labelList.append(shipLabel)

    def rebuildUI(self, sender, coordTuple, result):
        self.enemyLayout.removeWidget(sender)
        sender.deleteLater()
        cItem = QLabel(str(result))
        cItem.setStyleSheet("background: black; color: white; font-weight: bold;")
        cItem.setAlignment(Qt.AlignCenter)
        self.enemyLayout.addWidget(cItem, coordTuple[1], coordTuple[0])
    
    def rebuildUIbyPC(self, coordTuple, result):
        locNum = ((coordTuple[1] * 10) + coordTuple[0])
        currentLabel = self.labelList[locNum]
        currentLabel.setStyleSheet("background: red;")
        
    def prepareMissile(self):
        sender = self.sender()
        sendTuple = tuple(sender.text())
        sendSum = int(sendTuple[0]) + int(sendTuple[1])
        sendTuple = tuple((int(sendTuple[0]), int(sendTuple[1])))
        
        res = fireMissile(player2, sendTuple)
        if not (res):
            res = " "
        self.rebuildUI(sender, sendTuple, res)
        self.enemyLayout.update()
        
        """ Computer may fire now """
        returnedX, returnedY, returnedResult = fireAIMissile(player2)
        self.rebuildUIbyPC((returnedX, returnedY), returnedResult)
    
    def openWordList(self):
        wordsLength2 = randomWord(2, 1)
        wordsLength3 = randomWord(3, 1)
        wordsLength4 = randomWord(4, 1)
        
        buildString = "All the possible words are: \n \n"
        buildString += "Words with length 2:\n"
        for word in wordsLength2:
            buildString += word + ", "
        
        buildString += "\n\nWords with length 3:\n"
        for word in wordsLength3:
            buildString += word + ", "
        
        buildString += "\n\nWords with length 4:\n"
        for word in wordsLength4:
            buildString += word + ", "
            
            
        self.popupDict = TriggerPopup("Word list", buildString)
        self.popupDict.show()
        
        
    def endGame(self, yay):
        if (yay):
            title = "Congratulations!"
            text = "Congrats! You\'ve defeated the computer. Well done!"
        else:
            title = "Nawh, bummer"
            text = "Oops, you lost. Better luck next time!"
        

        self.popup = TriggerPopup(title, text)
        self.popup.setGeometry(QRect(100, 100, 400, 200))
        self.popup.show()
        self.close()
            
class GridView(QWidget):

    def __init__(self):
        super(GridView,self).__init__()
        self.buildUI2()
        self.shipNumber = 6
        self.shipLocations = []
        
    def buildUI2(self):
        ''' Build main grid '''
        self.itemLabel=[]
        self.selectedposition = (0,0)
        self.selecteddirection = "Horizontal"
        mainLayout = QGridLayout()
        mainLayout.setSpacing(5)
        self.ownLayout = QGridLayout()
        self.ownLayout.setSpacing(0)
        self.buildGrids2()
        self.setWindowTitle("Place your ships")
        self.shipCounter = 0
        
        ''' Place buttons '''
        placeShipButton = QPushButton("Place Ship")
        placeShipButton.clicked.connect(lambda: self.placeShip())
        self.directionBtn = QPushButton("Change to vertical", self)
        self.directionBtn.clicked.connect(lambda: self.direction())
        currentOrientationText = QLabel("Current orientation:")
        self.currentOrientation = QLabel("Horizontal")
        self.infoBar = QLabel("Status: Lay down a boat with length 2 on the grid")
        empty = QLabel("--------------------------------------------------------------------------------------")
        
        wrapper = QGridLayout()
        wrapper.addWidget(currentOrientationText, 0, 0)
        wrapper.addWidget(self.currentOrientation, 0, 1)
        
        mainLayout.addLayout(self.ownLayout, 0, 0)
        mainLayout.addWidget(self.infoBar, 1, 0)
        mainLayout.addWidget(empty, 2, 0)
        mainLayout.addWidget(placeShipButton, 3, 0)
        mainLayout.addWidget(empty, 4, 0)
        mainLayout.addLayout(wrapper, 5, 0)
        mainLayout.addWidget(self.directionBtn, 6, 0)

        self.setGeometry(300, 300, 400, 300)
        self.setLayout(mainLayout)
                  
    def buildGrids2(self):
        ''' Build own grid '''
        for i, item in enumerate(player.enemyGrid):
            itemStr = str(item[1])
            xCoord = item[0][0]
            yCoord = item[0][1]
            row, col = divmod(i, 10)
            self.itemLabel.append(QPushButton(str(col) + str(row), self))
            self.itemLabel[i].clicked.connect(lambda: self.selectPosition())
            self.itemLabel[i].setMaximumWidth(40)
            self.itemLabel[i].setStyleSheet("border: 1px solid #000;")
            self.ownLayout.addWidget(self.itemLabel[i], yCoord, xCoord)

        
    def placeShip(self):
        if (self.shipCounter < 2):
            num = 2
        elif (self.shipCounter < 4):
            num = 3
        else:
            num = 4
        
        self.shipCounter += 1
        
        if (self.shipCounter == 2):
            self.infoBar.setText("Status: Lay down a boat with length 3 on the grid")
        elif (self.shipCounter == 4):
            self.infoBar.setText("Status: Lay down a boat with length 4 on the grid")

        selectedposition = self.selectedposition
        selecteddirection = self.selecteddirection
        
        listIndex = (selectedposition[0] * 10) + selectedposition[1]
        
        if selecteddirection == "Horizontal":
            lijstvancoords = [(selectedposition[0]+i,selectedposition[1]) for i in range(num)]
        else:
            lijstvancoords = [(selectedposition[0],selectedposition[1]+i) for i in range(num)]
        
        randWord = randomWord(num, 0)
        self.fillcoords(randWord, lijstvancoords)
        
    def fillcoords(self, wordList, coords):
        looper = -1
        for i in coords:
            looper += 1
            self.shipLocations.append([(i[0], i[1]), wordList[looper]])
            app.processEvents()
            
            index = (i[1] * 10) + i[0]
            pushButton = self.itemLabel[index]
            self.ownLayout.removeWidget(pushButton)
            pushButton.deleteLater()
            cItem = QLabel(wordList[looper])
            cItem.setAlignment(Qt.AlignCenter)
            self.ownLayout.addWidget(cItem, i[1], i[0])
            
            
        self.shipNumber -= 1
        
        if (self.shipNumber == 0):
            startGame(self.shipLocations)
        
    def direction(self):
        if self.directionBtn.text() == "Change to vertical":
            self.directionBtn.setText("Change to horizontal")
            self.currentOrientation.setText("Vertical")
            self.selecteddirection = "Vertical"
        else:
            self.directionBtn.setText("Change to vertical")
            self.currentOrientation.setText("Horizontal")
            self.selecteddirection = "Horizontal"
	
    def selectPosition(self):
        sender = self.sender()
        sendTuple = tuple(sender.text())
        sendSum = int(sendTuple[0]) + int(sendTuple[1])
        sendTuple = tuple((int(sendTuple[0]), int(sendTuple[1])))
        self.selectedposition = sendTuple

def fireMissile(username, coordTuple):
    """ Vuur een missile op een username op locatie (x, y) """
    targetUser = username
    missileResult = targetUser.shipOnCoordinate(coordTuple)
    if (missileResult != 0):
        for location in targetUser.shipCoords:
            if ((location[0][0] == coordTuple[0]) and (location[0][1] == coordTuple[1])):
                targetUser.shipCoords.remove(location)
                stage2.statusBar.setText("BANG! That was a hit!")
                
        if (len(targetUser.shipCoords) == 0):
            stage2.endGame(1)
        
    else:
        stage2.statusBar.setText("You missed. Better luck next time ;)")    
    player.updateEnemyGrid(coordTuple, missileResult)
    return missileResult

def pickMissileLocation(missileList):
    gotMatch = 0
    xCoord = randrange(0, 10)
    yCoord = randrange(0, 10)
    
    for missile in missileList:
        if ((missile[0] == xCoord) and (missile[1] == yCoord)):
            return pickMissileLocation(missileList)
    
    return xCoord, yCoord
    
    
    
def fireAIMissile(computerPlayer):
    """ Kunstmatige Intelligentie (ofnouja, programmeerskills) """
    currentGrid = computerPlayer.getCurrentEnemyGrid()
    
    xCoord, yCoord = pickMissileLocation(currentGrid)

    missileResult = player.shipOnCoordinate((xCoord,yCoord))
    if (missileResult != 0):
        for location in player.shipCoords:
            if ((location.x == xCoord) and (location.y == yCoord)):
                player.shipCoords.remove(location)
                stage2.statusBar.setText("Awh, you've been hit!")
        if (len(player.shipCoords) == 0):
            stage2.endGame(0)
        
    computerPlayer.updateEnemyGrid((xCoord, yCoord), missileResult)
    
    return xCoord, yCoord, missileResult

def randomWord(num, getAll):
        if (num == 2):
            wordList = ["op", "af", "en", "ik", "we", "de", "je", "of", "as", 
            "al", "la", "nu", "af", "pa", "ma", "ex"]
        elif (num == 3):
            wordList = ["het", "dit", "wat", "wit", "rat", "bad", "bak", "kap", 
            "pik", "dat", "lol", "lip", "pil", "wil", "bam", "map", "wij",
            "jij", "hij", "zij", "mus", "ben"]
        else:
            wordList = ["waar", "trut", "shit", "mits", "stem", "pets",
            "date", "mens", "heks", "geel", "vlug", "stil", "haha", "game",
            "yolo", "ship", "boat"]
        
        randomWord = wordList[randrange(0, len(wordList))]
        randomWordList = list(randomWord)
        
        if (getAll):
            return wordList
        else:
            return randomWordList
        
def startGame(locList):
    stage1.close()
    
    shipList = []
    BattleShip = namedtuple("BattleShip", "x, y, letter")
    for ship in locList:
        ship1 = BattleShip(ship[0][0], ship[0][1], ship[1])
        shipList.append(ship1)
    
    
    player.placeShips(shipList)
    global stage2
    stage2 = GameView()
    stage2.show()

if __name__ == "__main__":
    player = NewPlayer("Johan")
    player2 = ComputerPlayer("Computer", 1)

    app = QApplication(sys.argv)
    stage1 = GridView()
    stage1.show()
    app.exec()
        


