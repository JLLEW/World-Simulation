from zwierzeta.zwierze import Zwierze
import random


class Lis(Zwierze):
    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 3
        self.priorytet = 7
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 3, 7, "red")
        else:
            super().__init__(swiat, 3, 7, "red", ruch, x, y)

    def klonowanie(self, swiat, x, y):
        return Lis(swiat, False, x, y)

    def akcja(self):
        powtorka = True
        ruch = True
        lewySilniejszy = False
        prawySilniejszy = False
        goraSilniejszy = False
        dolSilniejszy = False
        kierunek = ["gora", "dol", "lewo", "prawo"]

        self.obecnySwiat.plansza[self.y][self.x] = None

        while ruch:
            while powtorka and not (lewySilniejszy and prawySilniejszy and goraSilniejszy and dolSilniejszy):
                idz = random.choice(kierunek)
                powtorka = False
                self.prevY = self.y
                self.prevX = self.x
                if idz is "gora":
                    if not goraSilniejszy:
                        self.y -= 1
                    else:
                        powtorka = True
                elif idz is "dol":
                    if not dolSilniejszy:
                        self.y += 1
                    else:
                        powtorka = True
                elif idz is "lewo":
                    if not lewySilniejszy:
                        self.x -= 1
                    else:
                        powtorka = True
                else:
                    if not prawySilniejszy:
                        self.x += 1
                    else:
                        powtorka = True

            while self.x < 0:
                self.x += 1
            while self.x >= self.obecnySwiat.szerokosc:
                self.x -= 1
            while self.y < 0:
                self.y += 1
            while self.y >= self.obecnySwiat.wysokosc:
                self.y -= 1

            if self.obecnySwiat.plansza[self.y][self.x] is None:
                self.obecnySwiat.plansza[self.y][self.x] = self
                ruch = False
            elif self.obecnySwiat.plansza[self.y][self.x].sila <= self.sila:
                self.obecnySwiat.plansza[self.y][self.x].kolizja(self)
                ruch = False
            elif goraSilniejszy and dolSilniejszy and prawySilniejszy and lewySilniejszy:
                self.x = self.prevX
                self.y = self.prevY
                self.obecnySwiat.plansza[self.y][self.x] = self
                break
            else:
                if idz is "gora":
                    goraSilniejszy = True
                elif idz is "dol":
                    dolSilniejszy = True
                elif idz is "lewo":
                    lewySilniejszy = True
                else:
                    prawySilniejszy = True
                ruch = True
                self.x = self.prevX
                self.y = self.prevY
