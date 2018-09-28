from zwierzeta.zwierze import Zwierze

class CyberOwca(Zwierze):
    def __init__(self, swiat, ruch=False, x=-1, y=-1):
        self.sila = 11
        self.priorytet = 4
        self.obecnySwiat = swiat
        if x == -1:
            super().__init__(swiat, 11, 4, "aliceblue")
        else:
            super().__init__(swiat, 11, 4, "aliceblue", ruch, x, y)

    def klonowanie(self,swiat, x, y):
        return CyberOwca(swiat, False, x, y)

    def znajdzBarszcz(self):
        poprzedniaOdleglosc = 1000000000
        barszcz = None
        for organizm in self.obecnySwiat.listaOrganizmow:
            if organizm.__class__.__name__ is "BarszczSosnowskiego":
                x = abs(organizm.x - self.x)
                y = abs(organizm.y - self.y)
                odleglosc = x + y
                if odleglosc < poprzedniaOdleglosc:
                    barszcz = organizm
                    poprzedniaOdleglosc = odleglosc

        return barszcz

    def akcja(self):
        barszcz = self.znajdzBarszcz()
        if barszcz is None:
            super().akcja()
        else:
            self.obecnySwiat.plansza[self.y][self.x] = None
            x = self.x
            y = self.y
            if barszcz.x > x:
                self.x += 1
            elif barszcz.x < x:
                self.x -= 1
            elif barszcz.y > y:
                self.y += 1
            elif barszcz.y < y:
                self.y -= 1
            if self.obecnySwiat.plansza[self.y][self.x] is None:
                self.obecnySwiat.plansza[self.y][self.x] = self
            else:
                self.obecnySwiat.plansza[self.y][self.x].kolizja(self)


