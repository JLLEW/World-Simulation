from rosliny.roslina import Roslina
import random

class Trawa(Roslina):
    def __init__(self, swiat,ruch=False, x=-1, y=-1):
        self.sila = 0
        self.priorytet = 0
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 0, 0, "green")
        else:
            super().__init__(swiat, 0, 0, "green", ruch, x, y)

    def rozsiew(self, swiat, x, y):
        super().rozsiew(swiat, x, y)
        return Trawa(swiat, False, x, y)

    def indeks_rozsiewu(self):
        return random.randint(0, 99) >= 85

