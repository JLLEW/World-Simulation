from organizm import Organizm
from abc import ABC, abstractmethod
import random

class Roslina(Organizm, ABC):

    def __init__(self, swiat, sila, priorytet, color, ruch=False,  passedx=-1, passedy=-1):

        if passedx == -1:
            while True:
                x = random.randint(0, self.obecnySwiat.szerokosc - 1)
                y = random.randint(0, self.obecnySwiat.wysokosc - 1)
                if self.obecnySwiat.plansza[y][x] is None:
                    break
            ruch = True
        else:
            x = passedx
            y = passedy

        super().__init__(swiat, sila, priorytet, ruch, color, x, y)
        self.obecnySwiat.plansza[y][x] = self

    def akcja(self):
        x = self.x
        y = self.y

        if x + 1 < self.obecnySwiat.szerokosc and self.obecnySwiat.plansza[y][x+1] is None:
            x += 1
        elif x - 1 >= 0 and self.obecnySwiat.plansza[y][x - 1] is None:
            x -= 1
        elif y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[y + 1][x] is None:
            y += 1
        elif y - 1 >= 0 and self.obecnySwiat.plansza[y - 1][x] is None:
            y -= 1
        if self.indeks_rozsiewu() and self.obecnySwiat.plansza[y][x] is None:
           self.rozsiew(self.obecnySwiat, x, y)

    def indeks_rozsiewu(self):
        return random.randint(0, 99) > 70

    def kolizja(self, atakujacy):
        self.obecnySwiat.plansza[self.y][self.x] = atakujacy
        self.obecnySwiat.usun_organizm(self)
        self.komentator.komentuj_walke(atakujacy, self)

    def ucieczka(self, atakujacy):
        return False

    def obrona(self, atakujacy):
        return False

    def rozsiew(self, swiat, x, y):
        self.komentator.komentuj_rozsiew(self)



