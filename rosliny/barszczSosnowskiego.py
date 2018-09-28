from rosliny.roslina import Roslina
from zwierzeta.zwierze import Zwierze
import random

class BarszczSosnowskiego(Roslina):
    def __init__(self, swiat,ruch=False, x=-1, y=-1):
        self.sila = 10
        self.priorytet = 0
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 10, 0, "black")
        else:
            super().__init__(swiat, 10, 0, "black", ruch, x, y, )

    def rozsiew(self, swiat, x, y):
        super().rozsiew(swiat, x, y)
        return BarszczSosnowskiego(swiat, False, x, y)

    def indeks_rozsiewu(self):
        return random.randint(0, 99) >= 90

    def akcja(self):
        x = self.x
        y = self.y
        if x + 1 < self.obecnySwiat.szerokosc and self.obecnySwiat.plansza[y][x + 1] is not None:
            if issubclass(self.obecnySwiat.plansza[y][x + 1].__class__, Zwierze):
                klasa = self.obecnySwiat.plansza[y][x + 1].__class__.__name__
                klasa = str(klasa)
                if klasa != "CyberOwca":
                    self.obecnySwiat.usun_organizm(self.obecnySwiat.plansza[y][x + 1])
                    self.obecnySwiat.plansza[y][x + 1] = None
        if x - 1 >= 0 and self.obecnySwiat.plansza[y][x - 1] is not None:
            if issubclass(self.obecnySwiat.plansza[y][x - 1].__class__, Zwierze):
                klasa = self.obecnySwiat.plansza[y][x - 1].__class__.__name__
                klasa = str(klasa)
                if klasa != "CyberOwca":
                    self.obecnySwiat.usun_organizm(self.obecnySwiat.plansza[y][x - 1])
                    self.obecnySwiat.plansza[y][x - 1] = None
        if y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[y + 1][x] is not None:
            if issubclass(self.obecnySwiat.plansza[y + 1][x].__class__, Zwierze):
                klasa = self.obecnySwiat.plansza[y + 1][x].__class__.__name__
                klasa = str(klasa)
                if klasa != "CyberOwca":
                    self.obecnySwiat.usun_organizm(self.obecnySwiat.plansza[y + 1][x])
                    self.obecnySwiat.plansza[y + 1][x] = None
        if y - 1 >= 0 and self.obecnySwiat.plansza[y - 1][x] is not None:
            if issubclass(self.obecnySwiat.plansza[y - 1][x].__class__, Zwierze):
                klasa = self.obecnySwiat.plansza[y - 1][x].__class__.__name__
                klasa = str(klasa)
                if klasa != "CyberOwca":
                    self.obecnySwiat.usun_organizm(self.obecnySwiat.plansza[y - 1][x])
                    self.obecnySwiat.plansza[y - 1][x] = None
        super().akcja()

    def kolizja(self, atakujacy):
        self.obecnySwiat.plansza[self.y][self.x] = None
        if atakujacy.__class__.__name__ != "CyberOwca":
            self.obecnySwiat.usun_organizm(atakujacy)
        else:
            self.obecnySwiat.plansza[self.y][self.x] = atakujacy
        self.obecnySwiat.usun_organizm(self)
