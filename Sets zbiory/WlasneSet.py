from typing import List, Optional

class MySet:
    def __init__(self, tablica: Optional[List] = []):
        self.tablica = tablica

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
            return "błąd: próba usunięcia nie istniejącego elementu"

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
            else:
                raise TypeError(f"Nieobsługiwany typ: {type(element)}")

        self.tablica = nowaLista
        self.__update__()

        return MySet(nowaLista)


    def intersection(self, lista) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element in lista:
                NowaLista.append(element)
        self.tablica = NowaLista
        self.__update__()

        return MySet(NowaLista)

    def difference(self, lista) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element not in lista:
                NowaLista.append(element)
        self.tablica = NowaLista
        self.__update__()

        return MySet(NowaLista)
    
    def symmetric_difference(self, lista: list) -> "MySet":
        NowaLista = []
        for element in self.tablica:
            if element not in lista:
                NowaLista.append(element)
            else:
                lista.remove(element)
        for element in lista:
            NowaLista.append(element)
        self.tablica = NowaLista
        self.__update__()

        return MySet(NowaLista)

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

tablica = MySet([1, 2, 3])
print(tablica)
tablica.symmetric_difference([2, 3, 4])
print(tablica)








    # def copy(self):
    #     0

    # def clear(self) -> None:
    #     0

    # def __contains__(self) -> bool:
    #     0

    # def __len__(self) -> int:
    #     0

    # def __iter__(self):
    #     0

    # def __repr__(self) -> str:
    #     0

    # def __eq__(self) -> bool:
    #     0

