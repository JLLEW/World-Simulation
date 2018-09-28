from zwierzeta.zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, swiat, x=-1, y=-1):
        self.sila = 5
        self.priorytet = 4
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 5, 4, "aqua")
        else:
            super().__init__(swiat, 5, 4, "aqua", True, x, y)
        self.ruch = True

    def klonowanie(self, swiat, x, y): pass

    def akcja(self):
        print(self.sila)
        if self.sila > 5:
            self.sila -= 1
        if self.obecnySwiat.skill is True:
            self.aktywuj_umiejetnosc()
        idz = self.obecnySwiat.kierunek
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

    def aktywuj_umiejetnosc(self):
        self.sila = 10
        self.obecnySwiat.licznik = 5
        self.obecnySwiat.skill = False