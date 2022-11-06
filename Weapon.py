class Weapon:
    def __init__(self, range: int,ammunitions: int):
        self.__ammunitions = ammunitions
        self.__range = range

    def getRange(self):
        return self.__range

    def getAmmu(self):
        return self.__ammunitions

    def setAmmu(self,ammunitions: int):
        self.__ammunitions = ammunitions

    def fire_at(self,x: int, y: int, z: int):
        print(f"feu sur le point {x},{y},{z}")
        if self.__ammunitions == 0 :
            print("NoAmmunationError")
            return False
        else:
            self.__ammunitions = self.__ammunitions - 1
            return True


class Missile_anti_surface(Weapon):
    def __init__(self):
        super().__init__(30,40)
    def fire_at(self,x:int,y:int,z:int):
        if not super().fire_at(x,y,z):
            return False
        if z!=0:
            print("OutOFRangeError")
            self.setAmmu(self.getAmmu() - 1)
            return False
        return True


class Missile_anti_air(Weapon):
    def __init__(self):
        super().__init__(40,50)
    def fire_at(self,x:int,y:int,z:int):
        if not super().fire_at(x, y, z):
            return False
        if z <= 0:
            print("OutOFRangeError")
            self.setAmmu(self.getAmmu() - 1)
            return False
        return True

class Torpille(Weapon):
    def __init__(self):
        super().__init__(20,15)
    def fire_at(self,x:int,y:int,z:int):
        if not super().fire_at(self, x, y, z):
            return False
        if z > 0:
            print("OutOFRangeError")
            self.setAmmu(self.getAmmu() - 1)
            return False
        return True