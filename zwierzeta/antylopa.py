from zwierzeta.zwierze import Zwierze
import random

class Antylopa(Zwierze):
    def __init__(self, swiat, ruch=False , x=-1, y=-1):
        self.sila = 4
        self.priorytet = 4
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 4, 4, "chocolate")
        else:
            super().__init__(swiat, 4, 4, "chocolate", ruch, x, y)

    def klonowanie(self,swiat, x, y):
        return Antylopa(swiat, False, x, y)

    def akcja(self):
        kierunek = ["gora", "dol", "lewo", "prawo"]
        idz = random.choice(kierunek)
        self.prevX = self.x
        self.prevY = self.y
        self.obecnySwiat.plansza[self.y][self.x] = None

        if idz is "gora":
            self.y -= 2
        elif idz is "dol":
            self.y += 2
        elif idz is "lewo":
            self.x -= 2
        else:
            self.x += 2
        while self.x < 0:
            self.x = self.prevX
        while self.x >= self.obecnySwiat.szerokosc:
            self.x = self.prevX
        while self.y < 0:
            self.y = self.prevY
        while self.y >= self.obecnySwiat.wysokosc:
            self.y = self.prevY
        if self.obecnySwiat.plansza[self.y][self.x] is not None:
            self.obecnySwiat.plansza[self.y][self.x].kolizja(self)
        else:
            self.obecnySwiat.plansza[self.y][self.x] = self

    def ucieczka(self, atakujacy):
        czyUciekac = random.randint(0, 1) == 1
        if czyUciekac:
            if self.x + 1 < self.obecnySwiat.szerokosc and self.obecnySwiat.plansza[self.y][self.x + 1] is None:
                self.obecnySwiat.plansza[self.y][self.x + 1] = self
                self.obecnySwiat.plansza[self.y][self.x] = atakujacy
                self.x += 1
                return True
            elif self.x - 1 >= 0 and self.obecnySwiat.plansza[self.y][self.x - 1] is None:
                self.obecnySwiat.plansza[self.y][self.x - 1] = self
                self.obecnySwiat.plansza[self.y][self.x] = atakujacy
                self.x -= 1
                return True
            elif self.y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[self.y + 1][self.x] is None:
                self.obecnySwiat.plansza[self.y + 1][self.x] = self
                self.obecnySwiat.plansza[self.y][self.x] = atakujacy
                self.y += 1
                return True
            elif self.y - 1 >= 0 and self.obecnySwiat.plansza[self.y - 1][self.x] is None:
                self.obecnySwiat.plansza[self.y - 1][self.x] = self
                self.obecnySwiat.plansza[self.y][self.x] = atakujacy
                self.y -= 1
                return True
            else:
                return False
        else:
            return False
