from rosliny.roslina import Roslina
import random

class Mlecz(Roslina):
    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 0
        self.priorytet = 0
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 0, 0, "yellow")
        else:
            super().__init__(swiat, 0, 0, "yellow", ruch, x, y)

    def rozsiew(self, swiat, x, y):
        super().rozsiew(swiat, x, y)
        return Mlecz(swiat, False, x, y)

    def indeks_rozsiewu(self):
        czy = False
        i = 0
        while not czy and i < 3:
            czy = random.randint(0, 99) >= 75
            i += 1
        return czy