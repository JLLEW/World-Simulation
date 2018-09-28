from organizm import Organizm
from abc import ABC, abstractmethod
import random


class Zwierze(Organizm, ABC):

    def __init__(self, swiat, sila, priorytet, color, ruch=False, passedx=-1, passedy=-1):

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


    def obrona(self, atakujacy):
        return False

    def ucieczka(self, atakujacy):
        return False

    def akcja(self):
        kierunek = ["gora", "dol", "lewo", "prawo"]
        idz = random.choice(kierunek)
        self.prevX = self.x
        self.prevY = self.y
        self.obecnySwiat.plansza[self.y][self.x] = None

        if idz is "gora":
            self.y -= 1
        elif idz is "dol":
            self.y += 1
        elif idz is "lewo":
            self.x -= 1
        else:
            self.x += 1
        while self.x < 0:
            self.x += 1
        while self.x >= self.obecnySwiat.szerokosc:
            self.x -= 1
        while self.y < 0:
            self.y += 1
        while self.y >= self.obecnySwiat.wysokosc:
            self.y -= 1
        if self.obecnySwiat.plansza[self.y][self.x] is not None:
            self.obecnySwiat.plansza[self.y][self.x].kolizja(self)
        else:
            self.obecnySwiat.plansza[self.y][self.x] = self

    def kolizja(self, atakujacy):
        if atakujacy.__class__.__name__ == self.__class__.__name__ and atakujacy.ruch is True:
            atakujacy.obecnySwiat.plansza[atakujacy.prevY][atakujacy.prevX] = atakujacy
            atakujacy.x = atakujacy.prevX
            atakujacy.y = atakujacy.prevY
            self.rozmnazanie()
            self.komentator.komemntuj_rozmnazanie(self)
        elif not self.obrona(atakujacy):
            self.walka(atakujacy)
        elif not self.ucieczka(atakujacy):
            self.walka(atakujacy)

    def walka(self, atakujacy):
        if atakujacy.sila >= self.sila:
            self.komentator.komentuj_walke(atakujacy, self)
            self.obecnySwiat.plansza[self.y][self.x] = atakujacy
            self.obecnySwiat.usun_organizm(self)
        else:
            self.komentator.komentuj_walke(self, atakujacy)
            self.obecnySwiat.usun_organizm(atakujacy)

    def rozmnazanie(self):
        x = self.x
        y = self.y

        if x + 1 < self.obecnySwiat.szerokosc and self.obecnySwiat.plansza[y][x + 1] is None:
            x += 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif x - 1 >= 0 and self.obecnySwiat.plansza[y][x-1] is None:
            x -= 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[y + 1][x] is None:
            y += 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif y - 1 >= 0 and self.obecnySwiat.plansza[y - 1][x] is None:
            y -= 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif x + 1 < self.obecnySwiat.szerokosc and y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[y + 1][x + 1] is None:
            x += 1
            y += 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif x - 1 >= 0 and y - 1 >= 0 and self.obecnySwiat.plansza[y - 1][x - 1] is None:
            x -= 1
            y -= 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif x + 1 < self.obecnySwiat.szerokosc and y - 1 >= 0 and self.obecnySwiat.plansza[y - 1][x + 1] is None:
            x += 1
            y -= 1
            self.klonowanie(self.obecnySwiat, x, y)
            return
        elif x - 1 >= 0 and y + 1 < self.obecnySwiat.wysokosc and self.obecnySwiat.plansza[y + 1][x - 1] is None:
            x -= 1
            y += 1
            self.klonowanie(self.obecnySwiat, x, y)
            return

    @abstractmethod
    def klonowanie(self, swiat, x, y): pass


