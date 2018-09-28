from tkinter import *
class Swiat():

    listaOrganizmow = []
    poczekalnia = []
    plansza = []

    def __init__(self, szerokosc, wysokosc, root, canvas, licznik=0):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.root = root
        self.canvas = canvas
        self.kierunek = "prawo"
        self.skill = False
        self.licznik = licznik
        for y in range(0, wysokosc):
            self.plansza.append([])
            for x in range(0, szerokosc):
                self.plansza[y].append(None)
        self.cell_height = 450 / self.wysokosc
        self.cell_width = 450 / self.szerokosc


    def dodaj_organizm(self, organizm):
        self.listaOrganizmow.append(organizm)
        self.listaOrganizmow.sort(key = lambda x: x.priorytet, reverse=True)

    def dodaj_do_poczekalni(self, organizm):
        self.poczekalnia.append(organizm)
        self.poczekalnia.sort(key=lambda x: x.priorytet, reverse=True)

    def usun_organizm(self, organizm):
        if organizm in self.listaOrganizmow:
            self.listaOrganizmow.remove(organizm)
        elif organizm in self.poczekalnia:
            self.poczekalnia.remove(organizm)

    def wykonaj_ture(self):
        for organizm in self.listaOrganizmow:
            organizm.akcja()
        for organizm in self.poczekalnia:
            organizm.ruch = True
            self.dodaj_organizm(organizm)
            self.poczekalnia.remove(organizm)
        if self.licznik > 0:
            self.licznik -= 1
        self.rysuj_swiat()

    def rysuj_swiat(self):
        self.canvas.delete(ALL)
        for organizm in self.listaOrganizmow:
            organizm.rysuj()

    def drukuj_plansze(self):
        for data in self.plansza:
            print(data)

    def print_lista_organizmow(self):
        for organizm in self.listaOrganizmow:
            print(organizm.getNazwa() + " " + str(organizm.ruch))
    def zapisz(self):
        file = open('save.txt', 'w')
        file.write(str(self.szerokosc)+"\n")
        file.write(str(self.wysokosc)+"\n")
        file.write(str(self.skill)+"\n")
        file.write(str(self.licznik)+"\n")
        for organizm in self.listaOrganizmow:
            chain = organizm.__class__.__name__ + " " + str(organizm.sila) + " " + str(organizm.x) + " " + str(organizm.y)
            file.write(chain+"\n")
        file.close()
