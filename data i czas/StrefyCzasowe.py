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
        self.zamienniki_stref = {
            "poland": "Europe/Warsaw", "new_york": "America/New_York", "london": "Europe/London",
            "tokyo": "Asia/Tokyo", "sydney": "Australia/Sydney", "paris": "Europe/Paris",
            "berlin": "Europe/Berlin", "moscow": "Europe/Moscow", "los_angeles": "America/Los_Angeles",
            "cet": "CET", "cst6cdt": "America/Chicago", "cuba": "America/Havana",
            "eet": "EET", "est": "EST", "est5edt": "America/New_York",
            "egypt": "Africa/Cairo", "eire": "Europe/Dublin", "gb": "Europe/London",
            "gb-eire": "Europe/London", "gmt": "GMT", "gmt+0": "GMT",
            "gmt-0": "GMT", "gmt0": "GMT", "greenwich": "GMT",
            "hst": "HST", "hongkong": "Asia/Hong_Kong", "iceland": "Atlantic/Reykjavik",
            "iran": "Asia/Tehran", "israel": "Asia/Jerusalem", "jamaica": "America/Jamaica",
            "japan": "Asia/Tokyo", "kwajalein": "Pacific/Kwajalein", "libya": "Africa/Tripoli",
            "met": "CET", "mst": "MST", "mst7mdt": "America/Denver",
            "nz": "Pacific/Auckland", "nz-chat": "Pacific/Chatham", "navajo": "America/Denver",
            "prc": "Asia/Shanghai", "pst8pdt": "America/Los_Angeles", "portugal": "Europe/Lisbon",
            "roc": "Asia/Taipei", "rok": "Asia/Seoul", "singapore": "Asia/Singapore",
            "turkey": "Europe/Istanbul", "uct": "UCT", "utc": "UTC",
            "universal": "UTC", "w-su": "Europe/Moscow", "wet": "WET",
            "zulu": "UTC",
        }

        strefa = self.zamienniki_stref.get(strefa.lower(), strefa)

        print(f"Próba uzyskania godziny w strefie: {strefa}")

        try:
            strefaCzasowa = pytz.timezone(strefa)
            czasStrefowy = datetime.now(strefaCzasowa)
            print(f"Aktualna godzina w {strefa} wynosi: {czasStrefowy.strftime('%d %B %Y, %H:%M:%S')}")
        except pytz.UnknownTimeZoneError:
            print(f"Nieznana strefa czasowa: {strefa}")
        except Exception as e:
            print(f"Błąd: {e}")

    def konwertujCzas(self, strefaAktualna, strefaNowa, czas):
        
        czasZlokalizowany = strefaAktualna.localize(czas)
        czasZkonwertowany = czasZlokalizowany.astimezone(strefaNowa)
        print(f"Czas wejściowy: {czas}")
        print(f"Strefa aktualna: {strefaAktualna}")
        print(f"Strefa nowa: {strefaNowa}")

        return czasZkonwertowany
    
    @staticmethod
    def sprawdzCzasUTC():
        return str(datetime.now(pytz.utc))

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
        self.historiaDodaj("Wyświetlono klasę")
        
        for i, element in enumerate(self.historia):
            print(f"nr.{i + 1} : {element}")       

        print(f"Zapisana strefa: {self.zapisanaStrefa}")
        print("Class StrefyCzasowe dostepna" if StrefyCzasowe() else "Class StrefyCzasowe niedostepna")
        print("Class kontynent dostepna" if self.StrefyCzasowe.kontynent() else "Class StrefyCzasowe niedostepna")

        return f"Zapisana strefa: {self.zapisanaStrefa}"
    
    def historiaDodaj(self, dane):
        print(f"HISTORIA: {dane}")
        self.historia.append(dane)

    def zapiszStrefe(self, strefa:str = ""):
        try:
            pytz.timezone(strefa)
            self.historiaDodaj(f"Ustawiono zapisaną strefę na {strefa}")
            self.zapisanaStrefa = strefa
        except pytz.UnknownTimeZoneError:
            self.historiaDodaj(f"Dodana strefa nie była znaną")
            
    def wypiszStrefy(self, poczatek: int = 0, koniec: int = -1):
        self.historiaDodaj(f"Wypisano strefy od {str(poczatek)} do {str(len(self.StrefyCzasowe.slownikStrefCzas))}")
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

    def wyszukiwarka(self, baza, temat):
        self.historiaDodaj(f"zdefiniowano wyszukiwarę: {str(temat)}")
        def wyszukaj(baza: list[str], tekst: str):
            return [elemBaza for elemBaza in baza if tekst.lower() in elemBaza.lower()]

        print(f"Wyszukiwarka dla '{temat}', naciśnij 'Enter'. Wyjdź 'ESC'.")
        tekst = ""
        
        try:
            while True:
                event = keyboard.read_event(suppress=True)

                if event.event_type == "down":
                    if event.name == "esc":
                        print("\nZakończenie programu.")
                        return None
                    elif event.name == "enter":
                        print(f"\nWpisany tekst: {tekst}")
                        wyniki = wyszukaj(baza, tekst)
                        break
                    elif event.name == "backspace":
                        tekst = tekst[:-1] if tekst else ""
                    elif len(event.name) == 1:
                        tekst += event.name

                    wyniki = wyszukaj(baza, tekst)
                    print("\n" + "-"*30)
                    if wyniki:
                        print(f"Znalezione wyniki: {wyniki}")
                    else:
                        print(f"Brak wyników dla: {tekst}")
                    print("-"*30)

                    print(f"\nWyszukiwarka: {tekst}")

        finally:
            keyboard.unhook_all()
            
        if len(wyniki) == 1:
            return wyniki[0]
        elif len(wyniki) > 1:
            while True:
                print("\nDostępne wyniki:")
                for i, elem in enumerate(wyniki):
                    print(f"Nr.{i} : {elem}")

                try:
                    numer = int(input(f"\nPodaj numer wyniku od 0 do {len(wyniki) - 1}\nNumer: "))
                    if 0 <= numer < len(wyniki):
                        return wyniki[numer]
                    else:
                        print(f"Podano nieprawidłowy numer: {numer}")
                except ValueError:
                    print("Podano nieprawidłową wartość. Wpisz numer.")
        return None

    def wyszukajStrefe(self):
        self.historiaDodaj("Wyszukiwanie strefy czasowej")
        print("Wpisz nazwę strefy i naciśnij 'Enter'. Wyjdź 'ESC'.")
        
        wynik = self.wyszukiwarka(self.StrefyCzasowe.wszysStrefCzas, "strefa czasowa")
        self.historiaDodaj(f"Wyszukanie frazy: {wynik} się powiodło")

        if wynik:
            return wynik
        else:
            print("Brak wyników lub zakończenie programu.")
            return None
        
    def wyszukajKontynent(self):
        self.historiaDodaj("Wyszukiwanie kontynentu")
        wynik = self.wyszukiwarka(self.kontynent.kontynenty, "kontynent")
        self.historiaDodaj(f"Wyszukanie frazy: {str(wynik)} się powiodło")

        if wynik:
            return wynik
        else:
            print("Brak wyników lub zakończenie programu.")
            return None

    def wyswietlKontynenty(self):
        self.historiaDodaj("Wyświetlanie kontynentów")
        for kontynent in self.kontynent.wyswietl():
            print(kontynent)

    def sprawdzGodzine(self):
        self.historiaDodaj(f"Sprawdzanie godziny w strefie {str(self.zapisanaStrefa)}")
        self.StrefyCzasowe.sprawdzGodzine(self.zapisanaStrefa)

    def konwertujCzas(self, strefaAktualna: str, strefaNowa: str, rok: int = 0, miesiąc: int = 0, dzień: int = 0, godzina: int = 0, minuta: int = 0, sekunda: int = 0, mikroSekunda = 0):
        rok = int(rok)
        miesiąc = int(miesiąc)
        dzień = int(dzień)
        godzina = int(godzina)
        minuta = int(minuta)
        sekunda = int(sekunda)
        mikroSekunda = int(mikroSekunda)

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
                txt = str(czas.strftime("%d/%B/%Y, %H:%M:%S"))
                self.historiaDodaj(f"Konwertacja czasu: {txt}")

            except pytz.UnknownTimeZoneError:
                print(f"Nieznana strefa czasowa: {aktualnaStrefa} lub {nowaStrefa}")
                
            except Exception as e:
                print(f"Błąd podczas konwersji: {e}")

    def sprawdzCzasUTC(self):
        czas = self.StrefyCzasowe.sprawdzCzasUTC()
        self.historiaDodaj(f"Odczytano czas UTC wynoszący123: {str(czas)}")
        
        return czas

print(f"Program uruchomiony z pliku: {__name__}" + " <= plik główny" if __name__ == "__main__" else None)

program = Program()

print("\n> Test __str__")
program.__str__()

print("\n> Test historiaDodaj")
program.historiaDodaj("Test wpisu")
print(program.historia)

print("\n> Test zapiszStrefe")
program.zapiszStrefe("Europe/London")
print(program.zapisanaStrefa)

print("\n> Test wypiszStrefy")
print(program.wypiszStrefy(0, 5))

print("\n> Test wyszukajStrefe")
print(program.wyszukajStrefe())

print("\n> Test wyszukajKontynent")
print(program.wyszukajKontynent())

print("\n> Test wyswietlKontynenty")
program.wyswietlKontynenty()

print("\n> Test sprawdzGodzine")
program.sprawdzGodzine()

print("\n> Test konwertujCzas")
program.konwertujCzas("Europe/London", "America/New_York", 2024, 1, 31, 12, 0, 0)

print("\n> Test sprawdzCzasUTC")
print(program.sprawdzCzasUTC())
