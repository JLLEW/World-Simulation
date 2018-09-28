from tkinter import *
from swiat import Swiat
from zwierzeta.owca import Owca
from zwierzeta.lis import Lis
from zwierzeta.antylopa import Antylopa
from zwierzeta.cyberOwca import CyberOwca
from zwierzeta.wilk import Wilk
from zwierzeta.zolw import Zolw
from rosliny.guarana import Guarana
from rosliny.trawa import Trawa
from rosliny.wilczeJagody import WilczeJagody
from rosliny.mlecz import Mlecz
from rosliny.barszczSosnowskiego import BarszczSosnowskiego
from zwierzeta.czlowiek import Czlowiek


class gui:

    def __init__(self, root):
        self.canv = Canvas(root, bg="blue", height=450, width=450)
        self.root = root
        self.canv.pack()
        self.swiat = Swiat(10, 10, root, self.canv)
        Owca(self.swiat)
        Lis(self.swiat)
        Wilk(self.swiat)
        Antylopa(self.swiat)
        Zolw(self.swiat)
        Czlowiek(self.swiat)
        CyberOwca(self.swiat)
        WilczeJagody(self.swiat)
        Trawa(self.swiat)
        Mlecz(self.swiat)
        Guarana(self.swiat)
        BarszczSosnowskiego(self.swiat)
        Owca(self.swiat)
        Lis(self.swiat)
        Wilk(self.swiat)
        Antylopa(self.swiat)
        Zolw(self.swiat)
        CyberOwca(self.swiat)
        WilczeJagody(self.swiat)
        Trawa(self.swiat)
        Mlecz(self.swiat)
        Guarana(self.swiat)
        BarszczSosnowskiego(self.swiat)
        self.swiat.rysuj_swiat()
        self.button_frame = Frame(root)
        self.button_tura = Button(self.button_frame, text="nowa tura", command=self.tura).grid(row=5, column=0, sticky=W)
        self.button_umiejetnosc = Button(self.button_frame, text="specjalna umiejetnosc", command=self.specjalna).grid(row=5, column=1, sticky=W)
        self.button_zapisz = Button(self.button_frame, text="zapisz", command=self.zapis).grid(row=5, column=2, sticky=W)
        self.button_wczytaj = Button(self.button_frame, text="wczytaj", command=self.wczytaj).grid(row=5, column=3, sticky=W)
        self.button_frame.pack()
        self.rozmiar = Frame(root)
        self.szerokosc_spin = Spinbox(self.rozmiar, text="szerokosc", width=5, from_=5, to=100, wrap=True)
        self.szerokosc_spin.grid(row=0, column=0, sticky=E)
        self.wysokosc_spin = Spinbox(self.rozmiar, text="wysokosc", width=5, from_=5, to=100, wrap=True)
        self.wysokosc_spin.grid(row=0, column=1, sticky=E)
        self.button_nowy_swiat = Button(self.rozmiar, text="stworz swiat", command=self.nowy_swiat).grid(row=0, column=3, sticky=E)
        self.rozmiar.pack()


    def tura(self):
        self.swiat.wykonaj_ture()
    def specjalna(self):
        if self.swiat.licznik == 0:
            self.swiat.skill = True

    def zapis(self):
        self.swiat.zapisz()

    def wczytaj(self):
        file = open('save.txt', 'r')
        x = int(file.readline())
        y = int(file.readline())
        skill = bool(file.readline())
        counter = int(file.readline())
        self.swiat.listaOrganizmow.clear()
        self.swiat.poczekalnia.clear()
        for i in range(0, self.swiat.wysokosc - 1):
            for j in range(0, self.swiat.szerokosc - 1):
                self.swiat.plansza[i][j] = None
        self.canv.delete(ALL)
        self.swiat = Swiat(x, y, self.root, self.canv)
        for i in range(0, self.swiat.wysokosc - 1):
            for j in range(0, self.swiat.szerokosc - 1):
                self.swiat.plansza[i][j] = None
        self.swiat.licznik = counter
        self.swiat.skill = skill
        i = 0
        for line in file:
            line_array = line.split()
            class_name = line_array[0]
            strength = int(line_array[1])
            x = int(line_array[2])
            y = int(line_array[3])
            self.stworz_zwierze(class_name, strength, x, y, self.swiat)
        self.swiat.rysuj_swiat()
        file.close()

    def stworz_zwierze(self, klasa, sila, x, y, swiat):
        if klasa == "Zolw":
            nowy = Zolw(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Wilk":
            nowy = Wilk(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Owca":
            nowy = Owca(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Lis":
            nowy = Lis(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Czlowiek":
            nowy = Czlowiek(swiat,x, y)
            nowy.sila = sila
        elif klasa == "CyberOwca":
            nowy = CyberOwca(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Antylopa":
            nowy = Antylopa(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "WilczeJagody":
            nowy = WilczeJagody(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Trawa":
            nowy = Trawa(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Mlecz":
            nowy = Mlecz(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "Guarana":
            nowy = Guarana(swiat, True, x, y)
            nowy.sila = sila
        elif klasa == "BarszczSosnowskiego":
            nowy = BarszczSosnowskiego(swiat, True, x, y)
            nowy.sila = sila

    def nowy_swiat(self):
        x = int(self.szerokosc_spin.get())
        y = int(self.wysokosc_spin.get())
        self.canv.delete(ALL)
        self.swiat.listaOrganizmow.clear()
        self.swiat.poczekalnia.clear()
        for i in range(0, self.swiat.wysokosc - 1):
            for j in range(0, self.swiat.szerokosc - 1):
                self.swiat.plansza[i][j] = None
        self.swiat = Swiat(x, y, self.root, self.canv)
        for i in range(0, self.swiat.wysokosc - 1):
            for j in range(0, self.swiat.szerokosc - 1):
                self.swiat.plansza[i][j] = None
        Owca(self.swiat)
        Lis(self.swiat)
        Wilk(self.swiat)
        Antylopa(self.swiat)
        Zolw(self.swiat)
        Czlowiek(self.swiat)
        CyberOwca(self.swiat)
        WilczeJagody(self.swiat)
        Trawa(self.swiat)
        Mlecz(self.swiat)
        Guarana(self.swiat)
        BarszczSosnowskiego(self.swiat)
        self.swiat.wykonaj_ture()
        self.swiat.rysuj_swiat()

root = Tk()
root.resizable(False, False)
root.title("Virtual World Simulation 171646")
Gui = gui(root)

def left_key(event):
    Gui.swiat.kierunek = "lewo"
    Gui.swiat.wykonaj_ture()
def right_key(event):
    Gui.swiat.kierunek = "prawo"
    Gui.swiat.wykonaj_ture()

def up_key(event):
    Gui.swiat.kierunek = "gora"
    Gui.swiat.wykonaj_ture()


def down_key(event):
    Gui.swiat.kierunek = "dol"
    Gui.swiat.wykonaj_ture()

root.bind('<Left>', left_key)
root.bind('<Right>', right_key)
root.bind('<Up>', up_key)
root.bind('<Down>', down_key)
root.mainloop()
