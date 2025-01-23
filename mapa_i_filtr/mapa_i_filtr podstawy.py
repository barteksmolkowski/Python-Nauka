liczby = [2, 10, 12, 15, 20, 25, 30, 35]

# Mapy

def pomnóż(liczba):
    return liczba * 2

wynik = map(pomnóż, liczby)
print(list(wynik))

def parzyste(liczba):
    if liczba % 2 != 0:
        return liczba
    else:
        None

liczby = [1, 2, 3, 4, 5]
print(list(map(parzyste, liczby)))
print(list(map(lambda x: x**2, liczby)))

print(list(filter(lambda x: x % 2 == 0 , liczby)))

print("#####ZADANIA#####\nzad.numer: 1\n")

liczba = "12345"
wynik = "".join(map(lambda x: str(int(x) * 2), liczba))
print(wynik)

print("\nzad.numer: 2\n")

liczby = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, liczby)))

print("\nzad.numer: 3\n")

imiona = ["Anna", "Piotr", "Joanna", "Krzysztof", "Paulina", "Jan"]
print(list(filter(lambda imie: imie[0] in ["P", "p"], imiona)))

print("\nzad.numer: 4\n")

lista = [1, "abc", 3.5, 8, "123", None, 10, "hello"]

def CzyLiczba(tekst):
    try:
        liczba = int(tekst)
        return True
    except (ValueError, TypeError):
        return False

wynik = list(filter(CzyLiczba, lista))

liczby = list(map(float, wynik))

print(f"Suma liczb: {liczby} wynosi: {sum(liczby)}")

print("\nzad.numer: 5\n")

liczba = [3, 6, 15, 20, 23]
print(list(filter(lambda i: i if i % 3 == 0 or i % 5 == 0 else None, liczba)))

print("\nzad.numer: 6\n")

listaSłów = ["abc", "python", "code"]

NowaLista = list(map(lambda slowo: [i for i in slowo], listaSłów))
print(NowaLista)

print("\nzad.numer: 7\n")

liczby = [1, 2, 3, 4, 5]
print(list(map(lambda i: bin(i)[2:], liczby)))


print("\nzad.numer: 8\n")

tablica = ["hello", "world", "Python", "is", "awesome"]
print(list(filter(lambda słowo: słowo if len(słowo) >= 5 else None, tablica)))

print("\nzad.numer: 9\n")

liczby = [10, 50, 100, 150, 200]
kurs = 4.5
print(list(map(lambda liczba: round(liczba * kurs), liczby)))

print("\nzad.numer: 10\n")

lista = list([i for i in range(101)])
def CzyPierwsza(liczba):
    powtórki = liczba
    if liczba >= 10:
        powtórki = round(liczba ** 0.5)
    for i in range(powtórki):
        if i in [0, 1]:
            continue
        elif liczba % i == 0:
            return False
    return True

print(list(filter(CzyPierwsza, lista)))