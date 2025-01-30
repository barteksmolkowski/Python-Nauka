from datetime import datetime
import pytz
import re
import keyboard 

def dodajRE(tekst):
    znaki_zastępcze = {
        "a": "aą", "c": "cć", "e": "eę", "l": "lł",
        "n": "nń", "o": "oó", "s": "sś", "z": "zźż"
    }

    def zastąp_zgodność(znak):
        return f"[{znak}{znaki_zastępcze.get(znak.lower(), '')}]" if znak.lower() in znaki_zastępcze else re.escape(znak)

    return "^" + "".join(zastąp_zgodność(znak) for znak in tekst) + "$"

class StrefyCzasowe():
    def __init__(self):
        self.wszysStrefCzas = [strefa.lower() for strefa in pytz.all_timezones]
        wszysStrefCzasRE = [dodajRE(strefa) for strefa in self.wszysStrefCzas]

        self.populStrefCzas = [strefa.lower() for strefa in pytz.common_timezones]
        populStrefCzasRE = [dodajRE(strefa) for strefa in self.populStrefCzas]

        self.slownikStrefCzas = {}
        self.slownikPopulStrefCzas = {}

        for i in range(len(self.wszysStrefCzas)):
            self.slownikStrefCzas[self.wszysStrefCzas[i]] = wszysStrefCzasRE[i]
        for i in range(len(self.populStrefCzas)):
            self.slownikPopulStrefCzas[self.populStrefCzas[i]] = populStrefCzasRE[i]

        self.kontynenty = self.kontynent()

    def wypiszStrefy(self, poczatek, koniec):
        strefy = ""
        for i, strefa in enumerate(self.slownikStrefCzas):
            if poczatek <= i and i <= koniec:
                strefy += f"Strefa nr.{i - poczatek} : {strefa}"
        return strefy

    def wyszukaj(self, podanaStrefa: str):
        return [strefa for strefa in self.wszysStrefCzas if podanaStrefa.lower() in strefa.lower()]
    
    def sprawdzGodzine(self, strefa):
        try:
            strefaCzasowa = pytz.timezone(strefa)
            czasStrefowy = datetime.now(strefaCzasowa)
            print(strefaCzasowa)
            print(f"Aktualna godzina w {strefa} wynosi: {czasStrefowy.strftime('%H')}")
        except pytz.UnknownTimeZoneError:
            print("Nieznana strefa czasowa!")

    def konwertujCzas(self, strefaAktualna, strefaNowa, czas):
        
        czasZlokalizowany = strefaAktualna.localize(czas)
        czasZkonwertowany = czasZlokalizowany.astimezone(strefaNowa)
        print(f"Czas wejściowy: {czas}")
        print(f"Strefa aktualna: {strefaAktualna}")
        print(f"Strefa nowa: {strefaNowa}")

        return czasZkonwertowany

    def sprawdzCzasUTC():
        return datetime.now(pytz.utc)

    class kontynent():
        def __init__(self):
            self.kontynenty = ["Africa", "America", "Antarctica", "Asia", "Atlantic", "Australia", "Europe"]

        def wyszukaj(self, podanyKontynent: str):
            if not podanyKontynent.strip():
                print("Wpisano pusty ciąg. Zwracam pustą listę wyników.")
                return []
            
            wyszukaneKontynenty = []
            for kontynent in self.kontynenty:
                if kontynent.lower().startswith(podanyKontynent.lower()):
                    wyszukaneKontynenty.append(kontynent)
            
            print(f"Dla str: {podanyKontynent}. Znaleziono strefy: {wyszukaneKontynenty}")
            return wyszukaneKontynenty
        
        def wyswietl(self):
            for i, kontynent in enumerate(self.kontynenty):
                yield f"Kontynent {i}: {kontynent}"

class Program:
    def __init__(self):
        self.zapisanaStrefa = ""
        self.historia = []
        self.StrefyCzasowe = StrefyCzasowe()
        self.kontynent = self.StrefyCzasowe.kontynent()
        self.wpis = ""

    def __str__(self):
        print(f"""
              Zapisana strefa: {self.zapisanaStrefa}\n
              Historia: {self.historia}\n
              """)
        print("Class StrefyCzasowe dostepna" if StrefyCzasowe() else "Class StrefyCzasowe niedostepna")
        print("Class kontynent dostepna" if self.StrefyCzasowe.kontynent() else "Class StrefyCzasowe niedostepna")

    def zapiszStrefe(self, strefa:str = ""):
        self.zapisanaStrefa = strefa

    def wypiszStrefy(self, poczatek: int = 0, koniec: int = -1): # skończone
        error = ""
        if koniec == -1:
            koniec = len(self.StrefyCzasowe.slownikStrefCzas)
        elif poczatek < 0:
            error += "Podano ujemny początek\n"
        elif koniec < -1:
            error += "Podano ujemny koniec\n"
        elif poczatek > koniec:
            error += "Podano początek większy niż koniec\n"
        if error != "":
            return error
        else:
            strefy = self.StrefyCzasowe.wypiszStrefy(poczatek, koniec)

            return strefy

    def wyszukajStrefe(self):
        print("Wpisz nazwę strefy i naciśnij 'Enter'. Wyjdź 'ESC'.")

        try:
            while True:
                event = keyboard.read_event(suppress=True)
                
                if event.event_type == "down":
                    if event.name == "esc":
                        print("\nZakończenie programu.")
                        break
                    elif event.name == "enter":
                        print(f"\nWpisany tekst: {self.wpis}")
                        self.pokaz_wyniki()
                        break
                    elif event.name == "backspace":
                        self.wpis = self.wpis[:-1] if self.wpis else ""
                    elif len(event.name) == 1:
                        self.wpis += event.name

                    self.pokaz_wyniki()
                    print(f"Wyszukiwarka: {self.wpis}")
        finally:
            keyboard.unhook_all()
            wynik = self.pokaz_wyniki("end")
            if len(wynik) == 1:
                return wynik[0]
            else:
                wynikFalse = True
                while wynikFalse:
                    for i, strefa in enumerate(wynik):
                        print(f"Nr.{i} : {strefa}")
                    try:
                        numer = int(input(f"\nPodaj numer strefy od 0 do {len(wynik) - 1}\nNumer: "))
                        if 0 <= numer <= len(wynik) - 1:
                            return wynik[numer]
                        else:
                            print(f"Podano nie prawidlowy numer: {numer}")
                    except ValueError:
                        print(f"Podano nie prawidlowa fraza")

    def pokaz_wyniki(self, czyKoniec = None):
        wyniki = self.StrefyCzasowe.wyszukaj(self.wpis)

        if czyKoniec == "end":
            return wyniki
        
        print("\n" + "-"*30)
        if wyniki:
            print(f"Znalezione strefy: {wyniki}")
        else:
            print(f"Brak wyników dla: {self.wpis}")
        print("-"*30)

    def wyszukajKontynent(self): # podobna logika jak w def wyszukajStrefe(self)
        self.kontynent.wyszukaj("...")

    def wyswietlKontynenty(self):
        for kontynent in self.kontynent.wyswietl():
            print(kontynent)

    def sprawdzGodzine(self):# sprawdza godzine w self.zapisanaStrefa
        0 

    def konwertujCzas(self, strefaAktualna: str, strefaNowa: str, rok: int = 0, miesiąc: int = 0, dzień: int = 0, godzina: int = 0, minuta: int = 0, sekunda: int = 0, mikroSekunda = 0):
        txt = ""
        if miesiąc > 12:
            txt += "Podano nie prawidłowy miesiac\n"
        elif dzień > 31:
            txt += "Podano nie prawidłowy dzien\n"
        elif godzina >= 24:
            txt += "Podano nie prawidłową godzinę\n"
        elif minuta >= 60:
            txt += "Podano nie prawidłowa minute\n"
        elif sekunda >= 60:
            txt += "Podano nie prawidłowa sekunde\n"
        elif mikroSekunda > 999999:
            txt += "Podano nie prawidłowa milisekunda"
        
        if txt != "":
            print(txt)
            return None
        else:
            try:
                aktualnaStrefa = pytz.timezone(strefaAktualna)
                nowaStrefa = pytz.timezone(strefaNowa)
                czas = datetime(rok, miesiąc, dzień, godzina, minuta, sekunda, mikroSekunda)
                self.StrefyCzasowe.konwertujCzas(aktualnaStrefa, nowaStrefa, czas)

            except pytz.UnknownTimeZoneError:
                print(f"Nieznana strefa czasowa: {aktualnaStrefa} lub {nowaStrefa}")
                
            except Exception as e:
                print(f"Błąd podczas konwersji: {e}")

    def sprawdzCzasUTC(self):
        return self.StrefyCzasowe.sprawdzCzasUTC()

program = Program()
program.wyswietlKontynenty()
strefa = program.wyszukajStrefe()
print(f"znaleziono z wyszukiwarki strefe: {strefa}")
program.__str__()

