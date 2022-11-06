import Battlefield
from Vaisseaux import Vessel


class space:
    count = 0

    def __init__(self):
        self.__vaisseaux = []
        space.count += 1
        print(space.count, "Created")

    def getVaisseaux(self):
        return self.__vaisseaux

    def calcMaxHits(self):
        sum = 0
        for ves in self.__vaisseaux:
            sum += ves.get_MaxHits()
        return sum

    def addVaisseaux(self, vessel: Vessel, battlefield: Battlefield):
        cords = vessel.get_coordinates()
        if cords is None:
            print()
        else:
            x = cords[0]
            y = cords[1]
            z = cords[2]
            maxHits = self.calcMaxHits()
            if maxHits > 22 or maxHits + vessel.get_MaxHits() > 22:
                print("vessel pas ajouter à cause (MaxHits)")
            elif battlefield.checkPosition(x, y, z):
                print("vessel pas ajouter à cause (position)")
            else:
                self.__vaisseaux.append(vessel)
                battlefield.addVaisseaux(vessel)
                print("vessel ajouter avec succée")
