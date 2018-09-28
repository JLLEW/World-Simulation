from rosliny.roslina import Roslina
from zwierzeta.zwierze import Zwierze

import random


class Guarana(Roslina):

    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 0
        self.priorytet = 0
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 0, 0, "orange")
        else:
            super().__init__(swiat, 0, 0, "orange", ruch, x, y)

    def rozsiew(self, swiat, x, y):
        super().rozsiew(swiat, x, y)
        return Guarana(swiat, False, x, y)

    def indeks_rozsiewu(self):
        return random.randint(0, 99) >= 90

    def kolizja(self, atakujacy):
        if issubclass(atakujacy.__class__, Zwierze):
            atakujacy.sila += 3
        super().kolizja(atakujacy)
