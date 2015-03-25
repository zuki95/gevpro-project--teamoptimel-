"""
enemyGrid is hier een lege lijst waar enkel coördinaten in worden gezet
van missiles die zijn geschoten. Alle item zijn lists met coördinaten en
wel of geen hit ([x, y, 0] of [x, y, 1]).



Momenteel zet de computer zn boten soms op grid-punt 11, terwijl het maar
tot 10 loopt.. Iemand een geniale oplossing?

Het afvuren van missiles is ook pittig, want de computer moet weten wannneer
een boot is gezonken en dan verder gaan met nieuwe boten vinden ;(
"""

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
    
    def randomWord(num):
        if (num == 2):
            wordList = ["op", "af", "en", "ik", "we", "de", "je", "of", "as", 
            "al", "la", "nu", "af", "pa", "ma", "ex"]
        elif (num == 3):
            wordList = ["het", "dit", "wat", "wit", "rat", "bad", "bak", "kap", 
            "pik", "sex", "dat", "lol", "lip", "pil", "wil", "bam", "map", "wij",
            "jij", "hij", "zij", "mus", "ben"]
        else:
            wordList = ["waar", "trut", "shit", "mits", "stem", "pets", "seks",
            "date", "homo", "mens", "heks", "geel", "vlug", "stil", "haha"]
        
        randomWord = wordList[randrange(0, len(wordList))]
    
    return randomWord
    
    def placeShips(self):
        """ Zet schepen op random plekken neer """
        for i in range(2, 5):
            for j in range(2):
                xCoord = randrange(0, 10)
                yCoord = randrange(0, 10)
                random = bool(getrandbits(1))
                # random True/False for horizontal versus vertical placement
                shipWord = list(randomWord(i))
                
                newShip = self.createShip(xCoord, yCoord, i, random, [])
                
                for i in newShip:
                    self.shipCoords.append([newShip, shipWord[i]])
    
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
            if ((ship[0] == coordTuple[0]) and (ship[1] == coordTuple[1])):
                return 1
                
        return 0
    
    def getCurrentEnemyGrid(self):
        return self.enemyGrid
    
    def updateEnemyGrid(self, coordTuple, result):
        """ update de enemyGrid met een nieuwe status """
        self.enemyGrid.append([coordTuple[0], coordTuple[1], result]    )
        

def fireAIMissile(computerPlayer):
    """ Kunstmatige Intelligentie (ofnouja, programmeerskills) """
    currentGrid = computerPlayer.getCurrentEnemyGrid
    
    if (len(currentGrid) == 0): # First shot
        xCoord = randrange(0, 10)
        yCoord = randrange(0, 10)
        
        missileResult = computerPlayer.shipOnCoordinate((xCoord,yCoord))
        computerPlayer.updateEnemyGrid((xCoord, yCoord), missileResult)
        
    # Iemand een leuk idee hoe we kunnen zorgen dat de computer schepen
    # totaal de vernieling in schiet maar ook weet wanneer een ship is
    # verwoest zodat ie dan weer random kan gaan klooien? :D lastig gek.
            
    
    
    

# Om te testen:
def main():
    player = ComputerPlayer("johan", 1)
    print(player.shipCoords)
    
main()
