import Vaisseaux
from Vaisseaux import Vessel


class battlefield:

    def __init__(self):
        self.__vaisseaux = []
        print("Battlefield created")

    def getVaisseaux(self):
        return self.__vaisseaux

    def addVaisseaux(self, vessel: Vessel):
        self.__vaisseaux.append(vessel)


    def checkPosition(self, x: int, y: int, z: int):
        # if no ships exist
        if not self.__vaisseaux:
            return False
        for vessel in self.__vaisseaux:
            cords = vessel.get_coordinates()
            if cords[0] == x and cords[1] == y and cords[2] == z:
                return True
        return False


