from zwierzeta.zwierze import Zwierze
import random

class Zolw(Zwierze):

    def __init__(self, swiat,ruch=False, x=-1, y=-1):
        self.sila = 2
        self.priorytet = 1
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 2, 1, "olive")
        else:
            super().__init__(swiat, 2, 1, "olive", ruch, x, y)

    def klonowanie(self, swiat, x, y):
        return Zolw(swiat, False, x, y)

    def akcja(self):
        move = random.randint(1, 100) <= 25
        if move:
            super().akcja()

    def obrona(self, atakujacy):
        if atakujacy.sila < 5:
            self.obecnySwiat.plansza[atakujacy.prevY][atakujacy.prevX] = atakujacy
            atakujacy.x = atakujacy.prevX
            atakujacy.y = atakujacy.prevY
            return True
        return False
