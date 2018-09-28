from komentator import Komentator
from abc import ABC, abstractmethod

class Organizm(ABC):

    id = 0
    komentator = Komentator()
    def __init__(self, swiat, sila, priorytet, ruch, color, x, y):
        self.obecnySwiat = swiat
        self.id = Organizm.id
        self.sila = sila
        self.priorytet = priorytet
        self.ruch = ruch
        self.color = color
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        Organizm.id += 1
        if ruch:
            self.obecnySwiat.dodaj_organizm(self)
        else:
            self.obecnySwiat.dodaj_do_poczekalni(self)

    def rysuj(self):
        x = self.x
        y = self.y
        cell_width = self.obecnySwiat.cell_width
        cell_height = self.obecnySwiat.cell_height
        posx = x * cell_width
        posy = y * cell_height
        w_x = x * cell_width + cell_width
        w_y = y * cell_height + cell_height
        self.obecnySwiat.canvas.create_rectangle(posx, posy, w_x, w_y, fill=self.color)

    def getNazwa(self):
        return self.__class__.__name__ + " id: " + str(self.id)

    @abstractmethod
    def akcja(self): pass

    @abstractmethod
    def kolizja(self, atakujacy): pass

    @abstractmethod
    def obrona(self, atakujacy): pass

    @abstractmethod
    def ucieczka(self, atakujacy): pass


