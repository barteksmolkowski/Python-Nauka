print("lista = [3 ** i for i in range(20) if 3 ** i < 180000]")
nowa_lista = [3 ** i for i in range(20) if 3 ** i < 180000]
print(f"{nowa_lista}\n")

print("lista = [(i, i ** 2) for i in range(5)]")
nowa_lista = [(i, i ** 2) for i in range(5)]
print(f"{nowa_lista}\n")

print("lista = [{i : i ** 2} for i in range(5)]")
nowa_lista = [{i : i ** 2} for i in range(5)]
print(f"{nowa_lista}\n")

def funkcja(x):
    return x * 2

print("def funkcja(x):\n    return x*2")
print("lista = [funkcja(i) for i in range(5)]")
nowa_lista = [funkcja(i) for i in range(5)]
print(f"{nowa_lista}\n")

print("lista = [i for Clista in Zlista for i in Clista]")
Zlista = [[1, 2], [3, 4], [5, 6]]
nowa_lista = [i for Clista in Zlista for i in Clista]
print(f"{nowa_lista}\n")

lista = [-1, 5, 4, -9]
nowa_lista = [i if i >= 0 else 0 for i in lista]
print(f"{nowa_lista}\n")

nowa_lista = [print(f"{[i] * 10}") for i in range(10)]

zdanie = "(tekst): Witam tu Bartek"
nowa_lista = "".join([i.upper() if i != " " else "" for i in zdanie][9:])
print(f"{nowa_lista}\n")

zdanie = ["Witam", "tu", "Bartek"]
nowa_lista = [[litera for litera in slowo] for slowo in zdanie]
print(f"{nowa_lista}\n")

lista = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

nowa_lista = [i for rzad in lista for i in rzad]
print(f"{nowa_lista}\n")


liczby = [1,2,3,4,5,6,7,8,9]
nowa_lista = [i for i in liczby if i % 2 == 0]
print(f"{nowa_lista}\n")

slowa = ["siema", "tu", "bartek"]
nowa_lista = [i for i in slowa if len(i) == 2]
print(f"{nowa_lista}\n")

slowa = ["aba", "abcbd", "siemameis","próbabórlp"]

nowa_lista = [i for i in slowa if i == i[::-1]]
print(f"{nowa_lista}\n")

slowa = ["aba", "abcbd", "siemameis","próbabórlp"]
nowa_lista = [len(i) if i == i[::-1] else "-1" for i in slowa]
print(f"{nowa_lista}\n")

liczby = [12, 44, 10, 114]
bez_powtorzen = [i for i in liczby if len(set(str(i))) == len(str(i))]
print(f"Liczby bez powtórzeń: {bez_powtorzen}")