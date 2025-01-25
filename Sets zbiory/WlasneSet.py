from typing import List, Optional

class MySet:
    def __init__(self, nazwa: str, tablica: Optional[List] = None):
        self.tablica = tablica if tablica is not None else []
        self.nazwa = nazwa

    def __update__(self):
        NowaTab = []
        for element in self.tablica:
            if element not in NowaTab:
                NowaTab.append(element)
        self.tablica = NowaTab

    def __str__(self):
        self.__update__()
        tekst = "{" + ", ".join(map(str, self.tablica)) + "}"
        return tekst

    def add(self, element) -> None:
        self.tablica.append(element)
        self.__update__()

    def remove(self, element) -> None:
        if element in self.tablica:
            self.tablica.remove(element)
            self.__update__()
        else:
            raise ValueError("błąd: próba usunięcia nie istniejącego elementu")

    def discard(self, element) -> None:
        if element in self.tablica:
            self.tablica.remove(element)
            self.__update__()

    def union(self, lista) -> "MySet":
        nowaLista = self.tablica[:]
        for element in lista:
            if isinstance(element, list):
                for fragment in element:
                    nowaLista.append(fragment)
            elif isinstance(element, (str, int)):
                nowaLista.append(element)
        self.__update__()
        return MySet(self.nazwa, nowaLista)

    def intersection(self, lista) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element in lista:
                NowaLista.append(element)
        return MySet(self.nazwa, NowaLista)

    def difference(self, lista) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element not in lista:
                NowaLista.append(element)
        return MySet(self.nazwa, NowaLista)

    def symmetric_difference(self, lista: list) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element not in lista:
                NowaLista.append(element)
            elif element in lista:
                lista.remove(element)
        for element in lista:
            NowaLista.append(element)
        return MySet(self.nazwa, NowaLista)

    def isdisjoint(self, tablica) -> bool:
        for element in tablica:
            if element in self.tablica:
                return False
        return True

    def issubset(self, PodZbior) -> bool:
        for element in self.tablica:
            if element not in PodZbior:
                return False
        return True

    def issuperset(self, PodZbior) -> bool:
        for element in PodZbior:
            if element not in self.tablica:
                return False
        return True

    def copy(self):
        return self.tablica[:]
    
    def clear(self) -> None:
        self.tablica = []

    def __contains__(self, element) -> bool:
        return element in self.tablica

    def __len__(self) -> int:
        return len(self.tablica)

    def __iter__(self):
        return iter(self.tablica)

    def __repr__(self) -> str:
        return f"MySet(name={self.nazwa!r}, value={self.tablica!r})"

    def __eq__(self, tablica) -> bool:
        return sorted(self.tablica) == sorted(tablica)

# Import klasy MySet
from typing import List, Optional


def test_my_set():
    # Tworzenie zbioru
    zbior = MySet("TestowyZbior", [1, 2, 3, 3, 2])
    assert str(zbior) == "{1, 2, 3}", "Błąd w inicjalizacji i usuwaniu duplikatów."

    # Dodawanie elementów
    zbior.add(4)
    assert str(zbior) == "{1, 2, 3, 4}", "Błąd w dodawaniu elementów."

    # Próba dodania istniejącego elementu
    zbior.add(4)
    assert str(zbior) == "{1, 2, 3, 4}", "Błąd w obsłudze dodawania istniejących elementów."

    # Usuwanie elementów
    zbior.remove(2)
    assert str(zbior) == "{1, 3, 4}", "Błąd w usuwaniu elementów."

    # Próba usunięcia nieistniejącego elementu (spodziewamy się wyjątku)
    try:
        zbior.remove(5)
    except ValueError:
        pass  # Spodziewany wyjątek
    else:
        raise AssertionError("Błąd w obsłudze usuwania nieistniejących elementów.")

    # Wyczyść zbiór
    zbior.clear()
    assert str(zbior) == "{}", "Błąd w czyszczeniu zbioru."

    # Test sumy zbiorów
    zbior = MySet("A", [1, 2, 3])
    suma = zbior.union([3, 4, 5])
    assert str(suma) == "{1, 2, 3, 4, 5}", "Błąd w operacji sumy zbiorów."

    # Test przecięcia zbiorów
    przeciecie = zbior.intersection([2, 3, 4])
    assert str(przeciecie) == "{2, 3}", "Błąd w operacji przecięcia zbiorów."

    # Test różnicy zbiorów
    roznica = zbior.difference([3])
    assert str(roznica) == "{1, 2}", "Błąd w operacji różnicy zbiorów."

    # Test różnicy symetrycznej
    sym_diff = zbior.symmetric_difference([2, 3, 5])
    assert str(sym_diff) == "{1, 5}", "Błąd w różnicy symetrycznej."

    # Test isdisjoint
    assert zbior.isdisjoint([5, 6, 7]) is True, "Błąd w sprawdzaniu, czy zbiory są rozłączne."
    assert zbior.isdisjoint([2, 5]) is False, "Błąd w sprawdzaniu, czy zbiory nie są rozłączne."

    # Test issubset
    assert zbior.issubset([1, 2, 3, 4]) is True, "Błąd w sprawdzaniu podzbioru."
    assert zbior.issubset([2, 3]) is False, "Błąd w sprawdzaniu podzbioru."

    # Test issuperset
    assert zbior.issuperset([1, 2]) is True, "Błąd w sprawdzaniu nadzbioru."
    assert zbior.issuperset([5]) is False, "Błąd w sprawdzaniu nadzbioru."

    # Test copy
    kopia = zbior.copy()
    assert kopia == [1, 2, 3], "Błąd w kopiowaniu zbioru."

    # Test contains
    assert 2 in zbior, "Błąd w operatorze 'in'."
    assert 5 not in zbior, "Błąd w operatorze 'in'."

    # Test len
    assert len(zbior) == 3, "Błąd w zwracaniu liczby elementów."

    # Test iter
    assert list(iter(zbior)) == [1, 2, 3], "Błąd w iterowaniu zbioru."

    # Test eq
    assert zbior == [1, 2, 3], "Błąd w porównywaniu zbiorów."
    assert zbior != [1, 2], "Błąd w porównywaniu zbiorów."

    print("Wszystkie testy przeszły pomyślnie!")

test_my_set()