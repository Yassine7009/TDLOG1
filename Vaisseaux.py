from Weapon import Weapon


class Vessel:
    vaisseaux = []

    def __init__(self, coordinates: tuple, max_hits: int, weapon: Weapon):
        if 0 > (coordinates[0] or coordinates[1]) or 100 < (coordinates[0] or coordinates[1]) or coordinates[2] not in [
            -1, 0, 1]:
            print("Vous devez donner des coordonnées correctes")
            self.__coordinates = None
        else:
            self.__coordinates = coordinates
            self.__max_hits = max_hits
            self.__weapon = weapon

    @staticmethod
    def set_vaisseaux(vais):
        Vessel.vaisseaux = vais

    def go_to(self, x: int, y: int, z: int):
        try:
            self.__coordinates = (x, y, z)
        except self.__max_hits == 0:
            print("DestroyedError")

    def get_coordinates(self):
        return self.__coordinates

    def get_MaxHits(self):
        return self.__max_hits

    def set_MaxHits(self, MaxHits: int):
        self.__max_hits = MaxHits

    @staticmethod
    def getTheTarget(x: int, y: int, z: int):
        if not Vessel.vaisseaux:
            return None
        for vessel in Vessel.vaisseaux:
            cords = vessel.get_coordinates()
            if cords[0] == x and cords[1] == y and cords[2] == z:
                return vessel
        return None

    def fire_at(self, x: int, y: int, z: int):
        cords = self.get_coordinates()
        distance = (cords[0] - x) ^ 2 + (cords[1] - y) ^ 2 + (cords[2] - z) ^ 2
        if self.__max_hits == 0:
            print("DestroyedError")

        elif distance > self.__weapon.getRange():
            print("OutOfRange")
            self.__weapon.setAmmu(self.__weapon.getAmmu() - 1)

        else:
            bool = self.__weapon.fire_at(x, y, z)
            if bool:

                target = self.getTheTarget(x, y, z)
                target.set_MaxHits(target.get_MaxHits() - 1)
