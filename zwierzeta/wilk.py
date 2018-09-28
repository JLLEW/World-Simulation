from zwierzeta.zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, swiat,ruch=False, x=-1, y=-1):
        self.sila = 9
        self.priorytet = 5
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 9, 5, "gray")
        else:
            super().__init__(swiat, 9, 5,"gray", ruch, x, y)

    def klonowanie(self, swiat, x, y):
        return Wilk(swiat, False, x, y)

