from rosliny.roslina import Roslina
import random

class WilczeJagody(Roslina):
    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 99
        self.priorytet = 0
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 99, 0, "navy")
        else:
            super().__init__(swiat, 99, 0, "navy", ruch, x, y)

    def rozsiew(self, swiat, x, y):
        super().rozsiew(swiat, x, y)
        return WilczeJagody(swiat, False, x, y)

    def indeks_rozsiewu(self):
        return random.randint(0, 99) >= 95

    def kolizja(self, atakujacy):
        self.obecnySwiat.plansza[self.y][self.x] = None
        self.obecnySwiat.usun_organizm(atakujacy)
        self.obecnySwiat.usun_organizm(self)
