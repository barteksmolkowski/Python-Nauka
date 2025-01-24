class Produkt:
    def __init__(self, id_produktu, dostepnosc=True):
        self.id_produktu = id_produktu
        self.dostepnosc = dostepnosc

    def wydaj(self):
        if self.dostepnosc:
            self.dostepnosc = False
            print(f"Produkt {self.id_produktu} został wydany.")
        else:
            print(f"Produkt {self.id_produktu} już nie jest dostępny.")

    def zwroc(self):
        if not self.dostepnosc:
            self.dostepnosc = True
            print(f"Produkt {self.id_produktu} został zwrócony do magazynu.")
        else:
            print(f"Produkt {self.id_produktu} już jest dostępny.")

    def sprawdz_dostepnosc(self) -> bool:
        return self.dostepnosc
        
    def opisz_produkt(self):
        status = "dostępny" if self.dostepnosc else "niedostępny"
        print(f"Produkt o ID: {self.id_produktu} jest {status}.")


class Magazyn:
    def __init__(self):
        self.produkty = set()

    def dodaj_produkt(self, produkt):
        self.produkty.add(produkt)
        print(f"Dodano produkt o ID: {produkt.id_produktu}")

    def usun_produkt(self, id_produktu):
        for produkt in self.produkty:
            if produkt.id_produktu == id_produktu:
                self.produkty.remove(produkt)
                print(f"Usunięto produkt o ID: {id_produktu}")
                return
        print(f"Produkt o ID {id_produktu} nie został znaleziony w magazynie.")

    def wydaj_produkt(self, id_produktu):
        for produkt in self.produkty:
            if produkt.id_produktu == id_produktu:
                produkt.wydaj()
                return
        print(f"Produkt o ID {id_produktu} nie został znaleziony w magazynie.")

    def sprawdz_dostepnosc(self, id_produktu):
        for produkt in self.produkty:
            if produkt.id_produktu == id_produktu:
                status = "dostępny" if produkt.sprawdz_dostepnosc() else "niedostępny"
                print(f"Produkt o ID {id_produktu} jest {status}.")
                return
        print(f"Produkt o ID {id_produktu} nie został znaleziony w magazynie.")

    def zwroc_produkt(self, id_produktu):
        for produkt in self.produkty:
            if produkt.id_produktu == id_produktu:
                produkt.zwroc()
                return
        print(f"Produkt o ID {id_produktu} nie został znaleziony w magazynie.")

    def wypisz_dostepne_produkty(self):
        print("Lista dostępnych produktów:")
        for produkt in self.produkty:
            produkt.opisz_produkt()

    def zarzadzaj_magazynem(self):
        while True:
            print("\nMenu zarządzania magazynem:")
            print("1. Dodaj produkt")
            print("2. Usuń produkt")
            print("3. Wydaj produkt")
            print("4. Sprawdź dostępność produktu")
            print("5. Zwróć produkt")
            print("6. Wypisz wszystkie produkty")
            print("end - Wyjście")

            wybor = input("\nWybierz opcję: ").strip().lower()

            if wybor == "end":
                print("Zamykanie zarządzania magazynem.")
                break
            elif wybor == "1":
                id_produktu = input("Podaj ID produktu do dodania: ")
                self.dodaj_produkt(Produkt(id_produktu))
            elif wybor == "2":
                id_produktu = input("Podaj ID produktu do usunięcia: ")
                self.usun_produkt(id_produktu)
            elif wybor == "3":
                id_produktu = input("Podaj ID produktu do wydania: ")
                self.wydaj_produkt(id_produktu)
            elif wybor == "4":
                id_produktu = input("Podaj ID produktu do sprawdzenia: ")
                self.sprawdz_dostepnosc(id_produktu)
            elif wybor == "5":
                id_produktu = input("Podaj ID produktu do zwrócenia: ")
                self.zwroc_produkt(id_produktu)
            elif wybor == "6":
                self.wypisz_dostepne_produkty()
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")


# Przykładowe użycie:
magazyn = Magazyn()
magazyn.zarzadzaj_magazynem()
