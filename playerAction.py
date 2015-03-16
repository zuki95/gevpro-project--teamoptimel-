"""
NewPlayer wordt voor elke speler aangemaakt bij het starten van een spel. De
class houdt alle gegevens van een speler bij (de GUI kan hier dus de gegevens
uit halen om weer te geven).

Ingebouwd:
    name            Naam (wordt aangeroepen bij initialiseren)
    shipCoords      Coordinaten van de schepen van de gebruiker als
                    namedtuple (x, y, letter)

Moet nog:
    shotsFired      Een list/dict/whatever waar per coordinaat bijgehouden wordt
                    of er al op geschoten is en wat het eventuele resultaat van
                    dat schot was (no-hit of de letter van de hit)
"""

from collections import namedtuple

class NewPlayer:
    def __init__(self, name):
        """ name wordt meegegeven aan de __init__, shipCoords is een lege list """
        self.name = name
        self.shipCoords = []
    
    def placeShips(self, coordsList):
        """
        Krijgt een lijst van coordinaten (als namedtuple (x, y, letter))
        mee om te plaatsen: BattleShip = namedtuple('BattleShip', 'x, y, letter')
                            new_ship = BattleShip(4, 6, 'L')
        """
        self.shipCoords = coordsList
    
    def shipOnCoordinate(self, x, y):
        """ checkt of er een schip is op de plek van het schot """
        for ship in self.shipCoords:
            if ((ship.x == x) and (ship.y == y)):
                return ship.letter
                
        return False


def fireMissile(username, x, y):
    """ Vuur een missile op een username op locatie (x, y) """
    targetUser = username
    
    return targetUser.shipOnCoordinate(x, y)


# Om te testen:
def main():
    player = NewPlayer("johan")
    BattleShip = namedtuple("BattleShip", "x, y, letter")
    shipList = []
    
    myFirstRealShipOMG = BattleShip(2, 6, "L")
    shipList.append(myFirstRealShipOMG)
    player.placeShips(shipList)
    
    # Returnt False (want schip is op 2,6)
    print(fireMissile(player, 3, 6))
    
    # Returnt de letter "L"
    print(fireMissile(player, 2, 6))
    
main()
