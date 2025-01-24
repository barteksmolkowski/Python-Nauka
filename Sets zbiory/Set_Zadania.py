import random

##### ZADANIE 1 #####

print(set([1, 2, 3, 3, 4, 5, 1, 2]))

##### ZADANIE 2 #####

lista = {1, 2, 3, 4}
lista.add(5)
print(lista)

##### ZADANIE 3 #####

lista = {10, 20, 30, 40}
lista.remove(30)
print(lista)

##### ZADANIE 4 #####

lista = {10, 20, 30, 40}
liczba = random.choice(list(lista))
lista.remove(liczba)
print(f"{lista} a usunięto: {liczba}")

##### ZADANIE 5 #####

lista = {10, 20, 30, 40}
lista.clear()
print("Lista jest pusta" if lista == set() else "Lista nie jest pusta")

##### ZADANIE 6 #####

lista = {10, 20, 30, 40}
lista2 = lista.copy()
print("Listy są te same" if lista == lista2 else "Listy nie są te same")

##### ZADANIE 7 #####

setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA.union(setB))

##### ZADANIE 8 #####

setA = {1, 2, 3}
setB = {2, 3, 4}
setC = setA.intersection(setB)
print(setC)

##### ZADANIE 9 #####

setA = {1, 2, 3}
setB = {2, 3, 4}
setC = setA.difference(setB)
print(setC)

##### ZADANIE 10 #####

setA = {1, 2}
setB = {3, 4}
setC = {5, 6}

setD = setA.union(setB.union(setC))
print(setD)