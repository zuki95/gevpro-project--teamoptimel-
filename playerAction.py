"""
NewPlayer wordt voor elke speler aangemaakt bij het starten van een spel. De
class houdt alle gegevens van een speler bij (de GUI kan hier dus de gegevens
uit halen om weer te geven).

Ingebouwde variabelen:
    name            Naam (wordt aangeroepen bij initialiseren)
    shipCoords      Coordinaten van de schepen van de gebruiker als
                    namedtuple (x, y, letter)
    enemyGrid       Een list van lists. Deze lists bevatten een tuple
                    voor de coordinaten en een item voor de waarde,
                    bv: [(2, 6), "H"]. Dit lijkt omslachtig, maar omdat
                    tuples immutable zijn is een een (named)tuple hier
                    niet te gebruiken.

Ingebouwde methoden:
    placeShips:     Voor het plaatsen van schepen. Moet een lijst van namedtuples
                    krijgen: ... = namedtuple('...', 'x, y, letter')
    
    shipOnCoordinate: Checkt of er op het opgegeven coordinaat een schip aanwezig
                    is. Krijgt coordinaten als tuple (x, y) mee en returnt de
                    eventuele letter of False.
    
    updateEnemyGrid: Werkt het resultaat van een schot bij in de enemyGrid lijst.
    
Enkele tips:
    Coordinaten:    Altijd weergeven als tuple. Dit is overzichtelijk (want
                    is gelijk wiskunde notatie (x, y)) en bovendien immutable
                    dus niet per ongeluk te verpesten met een fout stukje code.
    
    Opbouw grid:    De grid kan worden opgebouwd uit de self.enemyGrid lijst.
                    Deze lijst bevat, naast de coordinaten, ook een 'status':
                    0:      Nog geen missile op deze coordinaten afgevuurd
                    1:      Wel een missile afgevuurd, maar geen hit
                    "x":    Missile was een hit, de status bevat nu de
                            corresponderende letter.
    
"""

from collections import namedtuple

class NewPlayer:
    def __init__(self, name):
        """
        Class om een nieuwe speler aan te maken. Aan te roepen via
        nieuwe_speler = NewPlayer("gebruikersnaam")
        """
        self.name = name
        self.shipCoords = []
        self.enemyGrid = []
        
        # Fill a list with all grid points and set them empty for the time being
        for y in range(10):
            for x in range(10):
                tempList = [(x, y), 0]
                self.enemyGrid.append(tempList)
    
    def placeShips(self, coordsList):
        """
        Krijgt een lijst van coordinaten (als namedtuple (x, y, letter)) mee
        """
        self.shipCoords = coordsList
    
    def shipOnCoordinate(self, coordTuple):
        """ checkt of er een schip is op de plek van het schot """
        for ship in self.shipCoords:
            if ((str(ship.x) == str(coordTuple[0])) and (str(ship.y) == str(coordTuple[1]))):
                return ship.letter 
        return 1
    
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

"""
# Om te testen:
def main():
    player = NewPlayer("johan")
    BattleShip = namedtuple("BattleShip", "x, y, letter")
    shipList = []
    
    myFirstRealShipOMG = BattleShip(2, 6, "L")
    shipList.append(myFirstRealShipOMG)
    player.placeShips(shipList)
    
    # Returnt 1 (want schip is op (2,6))
    print(fireMissile(player, (3, 6)))
    
    # Returnt de letter "L"
    print(fireMissile(player, (2, 6)))
    
    # Returnt de huidige enemyGrid-lijst
    #print(player.enemyGrid)
    
    # Print een overzichtelijke enemyGrid
    gridList = ""
    for x in range(10):
        for y in range(10):
            number = (x * 10) + y
            gridList += str(player.enemyGrid[number][1]) + " "
        
        gridList += "\n"
    
    print(gridList)
    
main()
"""
