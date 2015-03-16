"""
Documentatie volgt.
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
        
        # Fill a list with all grid points and set them empty for the time being
        for x in range(10):
            for y in range(10):
                tempList = [x, y, 0]
                self.enemyGrid.append(tempList)
        
        self.placeShips()
    
    def placeShips(self):
        """ Zet schepen op random plekken neer """
        for i in range(2, 4):
            for j in range(2):
                xCoord = randrange(0, 10)
                yCoord = randrange(0, 10)
                random = bool(getrandbits(1))
                # random True/False for horizontal versus vertical placement
                
                newShip = self.createShip(xCoord, yCoord, i, random, [])
                
                self.shipCoords.extend(newShip)
    
    def createShip(self, xCoord, yCoord, shipSize, isHorizontal, shipCoordsList):
        """
        xCoord = yCoord are coordinates, shipSize is the size (2-4 blocks) of
        the ship, isHorizontal is randomly True/False for the orientation and
        the shipCoordsList is filled with coordinates.
        """
        
        if(len(shipCoordsList) == shipSize):
            return shipCoordsList
        
        if(self.shipOnCoordinate((xCoord, yCoord))):
            return 0
        
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
            if ((ship.x == coordTuple[0]) and (ship.y == coordTuple[1])):
                return ship.letter
                
        return 0
    
    def updateEnemyGrid(self, coordTuple, statusStr):
        """ update de enemyGrid met een nieuwe status """
        for gridItem in self.enemyGrid:
            if (gridItem[0] == coordTuple):
                gridItem[1] = statusStr


def fireMissile(username, coordTuple):
    """ Vuur een missile op een username op locatie (x, y) """
    targetUser = username
    missileResult = targetUser.shipOnCoordinate(coordTuple)
    
    targetUser.updateEnemyGrid(coordTuple, missileResult)
 
    return missileResult


# Om te testen:
def main():
    player = ComputerPlayer("johan", 1)
    
    # Print een overzichtelijke enemyGrid
    gridList = ""
    for x in range(10):
        for y in range(10):
            number = (x * 10) + y
            gridList += str(player.enemyGrid[number][1]) + " "
        
        gridList += "\n"
    
    print(gridList)
    
main()
