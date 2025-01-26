import pytz
from datetime import datetime

for i in pytz.all_timezones:
    print(i)



class StrefyCzasowe():
    def __init__(self):
        self.wszysStrefCzas = [strefa.lower() for strefa in pytz.all_timezones]
        self.populStrefCzas = [strefa.lower() for strefa in pytz.common_timezones]
        self.strefa = ""
        
        self.kontynenty = self.kontynent()

    def wyszukaj(self, podanaStrefa: str):
        wyszukaneStrefy = []
        for strefa in self.wszysStrefCzas:
            # Sprawdzanie, czy podanaStrefa zaczyna się od strefy
            if podanaStrefa.lower().startswith(strefa.lower()):
                wyszukaneStrefy.append(strefa)
        print(f"Dla str: {podanaStrefa}. Znaleziono strefy: {wyszukaneStrefy}")
        return wyszukaneStrefy

    def sprawdzGodzine(self, strefa):
        try:
            strefaCzasowa = pytz.timezone(strefa)
            czasStrefowy = datetime.now(strefaCzasowa)
            print(strefaCzasowa)
            print(f"Aktualna godzina w {strefa} wynosi: {czasStrefowy.strftime('%H')}")
        except pytz.UnknownTimeZoneError:
            print("Nieznana strefa czasowa!")

    def listujStrefy(self):
        0

    def sprawdzCzasUTC():
        0

    def konwertujCzas(strefa1, strefa2):
        0  # Metoda do konwersji czasu z jednej strefy na inną.

    class kontynent():
        def __init__(self):
            self.kontynenty = ["Africa", "America", "Antarctica", "Asia", "Atlantic", "Australia", "Europe"]

        def wyszukaj(self, podanyKontynent: str):
            wyszukaneKontynenty = []
            for kontynent in self.kontynenty:
                if podanyKontynent.lower().startswith(kontynent.lower()):
                    wyszukaneKontynenty.append(kontynent)
            print(f"Dla str: {podanyKontynent}. Znaleziono strefy: {wyszukaneKontynenty}")
            return wyszukaneKontynenty
        
        def wyswietl(self):
            string = ""
            for i, kontynent in enumerate(self.kontynenty):
                string += f"Kontynent {i}: {kontynent}\n"
            return string

strefyczasowe = StrefyCzasowe()

print(strefyczasowe.wyszukaj("o"))
print(strefyczasowe.kontynenty.wyswietl())

