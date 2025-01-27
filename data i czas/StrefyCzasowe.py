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

    def konwertujCzas(self, strefaAktualna, strefaNowa, rok = 0, miesiąc = 0, dzień = 0, godzina = 0, minuta = 0, sekunda = 0, mikroSekunda = 0):
        if miesiąc > 12 or dzień > 31 or godzina >= 24 or minuta >= 60 or sekunda >= 60 or mikroSekunda > 999999:
            print("Podano nie prawidłową godzinę")
            return None
        czas = datetime(rok, miesiąc, dzień, godzina, minuta, sekunda, mikroSekunda)
        try:
            aktualnaStrefa = pytz.timezone(strefaAktualna)
            nowaStrefa = pytz.timezone(strefaNowa)

            czasZlokalizowany = aktualnaStrefa.localize(czas)
            czasZkonwertowany = czasZlokalizowany.astimezone(nowaStrefa)
            print(f"Czas wejściowy: {czas}")
            print(f"Strefa aktualna: {strefaAktualna}")
            print(f"Strefa nowa: {strefaNowa}")

            return czasZkonwertowany
        
        except pytz.UnknownTimeZoneError:
            print(f"Nieznana strefa czasowa: {strefaAktualna} lub {strefaNowa}")
        except Exception as e:
            print(f"Błąd podczas konwersji: {e}")

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
            string = ""
            for i, kontynent in enumerate(self.kontynenty):
                string += f"Kontynent {i}: {kontynent}\n"
            return string

strefyczasowe = StrefyCzasowe()

# Test wyszukaj - poprawne dane
print("Test wyszukaj:")
wynik_wyszukaj = strefyczasowe.wyszukaj("Europe")
print(f"Znalezione strefy dla 'Europe': {wynik_wyszukaj}")

# 2. Test funkcji wyszukaj - brak wyników
print("\nTest wyszukaj - brak wyników:")
wynik_wyszukaj_pusty = strefyczasowe.wyszukaj("XYZ")
print(f"Znalezione strefy dla 'XYZ': {wynik_wyszukaj_pusty}")
assert len(wynik_wyszukaj_pusty) == 0, "Funkcja wyszukaj powinna zwrócić pustą listę."

# 3. Test funkcji sprawdzGodzine - poprawne dane
print("\nTest sprawdzGodzine:")
strefyczasowe.sprawdzGodzine("Europe/Warsaw")

# 4. Test funkcji sprawdzGodzine - błędna strefa czasowa
print("\nTest sprawdzGodzine - błędna strefa czasowa:")
strefyczasowe.sprawdzGodzine("Invalid/Zone")

# 5. Test funkcji konwertujCzas - poprawna konwersja
print("\nTest konwertujCzas:")
skonwertowany_czas = strefyczasowe.konwertujCzas("Europe/Warsaw", "America/New_York", 2021, 5, 20, 20, 5)
print(f"Skonwertowany czas: {skonwertowany_czas}")

# 6. Test funkcji konwertujCzas - błędne dane wejściowe
print("\nTest konwertujCzas - błędna data:")
strefyczasowe.konwertujCzas("Europe/Warsaw", "America/New_York", 2021, 11, 20, 25, 61)

# 7. Test funkcji sprawdzCzasUTC
print("\nTest sprawdzCzasUTC:")
czas_utc_test = StrefyCzasowe.sprawdzCzasUTC()
print(f"Czas UTC: {czas_utc_test}")
assert isinstance(czas_utc_test, datetime), "Funkcja sprawdzCzasUTC powinna zwracać obiekt datetime."

# 8. Test funkcji wyswietl w kontynentach
print("\nTest kontynent.wyswietl:")
kontynenty_wyswietl = strefyczasowe.kontynenty.wyswietl()
print(kontynenty_wyswietl)
assert "Kontynent" in kontynenty_wyswietl, "Funkcja wyswietl powinna wypisać listę kontynentów."

# 9. Test funkcji wyszukaj w kontynentach
print("\nTest kontynent.wyszukaj:")
kontynenty_wyszukaj = strefyczasowe.kontynenty.wyszukaj("Amer")
print(f"Znalezione kontynenty: {kontynenty_wyszukaj}")
assert "America" in kontynenty_wyszukaj, "Funkcja wyszukaj powinna znaleźć kontynent 'America'."

# 10. Test wyszukiwania w pustej lub krótkiej strefie
print("\nTest wyszukaj - pusta strefa:")
wynik_pusty = strefyczasowe.wyszukaj("a")
print(f"Znalezione strefy dla pustego stringa: {wynik_pusty}")

# 11. Test poprawności obsługi wyjątków w konwersji
print("\nTest konwertujCzas - nieznana strefa:")
strefyczasowe.konwertujCzas("Nieznana/Strefa", "Invalid/Zone", 2021, 5, 20, 20, 5)
