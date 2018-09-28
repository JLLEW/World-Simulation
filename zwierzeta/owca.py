from zwierzeta.zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 4
        self.priorytet = 4
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 4, 4, "snow")
        else:
            super().__init__(swiat, 4, 4, "snow", ruch, x, y)

    def klonowanie(self, swiat, x, y):
        return Owca(swiat, False, x, y)


