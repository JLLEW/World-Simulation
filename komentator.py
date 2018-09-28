
class Komentator:
    def komentuj_walke(self, wygrany, przegrany):
        x = str(przegrany.x)
        y = str(przegrany.y)
        print(wygrany.getNazwa() + " zjadl " + przegrany.getNazwa() + " na pozycji: " + x + " " + y)
    def komemntuj_rozmnazanie(self, gatunek):
        x = str(gatunek.x)
        y = str(gatunek.y)
        print(gatunek.getNazwa() + " rozmnozyl sie na pozycji: " + x + " " + y)
    def komentuj_rozsiew(self, gatunek):
        x = str(gatunek.x)
        y = str(gatunek.y)
        print("gatunek " + gatunek.getNazwa() + " rozsial sie na pozycji: " + x + " " + y)