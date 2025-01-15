import re

print("##### ZADANIE 1 #####")

wynik = re.match(r"(?P<imię>[A-Za-z0-9]{3,}).(?P<nazwisko>[A-Za-z0-9]{3,})@(?P<strona>[A-Za-z]{3,6}).(?P<witryna>[A-Za-z]{1,5})", "bartek.smolkowski@gmail.com")
if wynik:
    print(f"Dopasowano!")
    print(f"Imię: {wynik.group('imię')}")
    print(f"Nazwisko: {wynik.group('nazwisko')}")
    print(f"Strona: {wynik.group('strona')}")
    print(f"Witryna: {wynik.group('witryna')}")
else:
    print("Nie dopasowano")


print("\n\n##### ZADANIE 2 #####")

tekst = "Rok 2025, cena to 10,000.99 zł"
NowyTekst = tekst.replace(",", "").replace(".", "")
lista = re.findall(r"[0-9]+", f"{NowyTekst}")
print("Oczyszczony tekst:", NowyTekst)
print("Lista liczb:", lista)


print("\n\n##### ZADANIE 3 #####")

tekst = "+48 123 456 789"
wynik = re.match(r"^\+(?P<kierunek>[0-9]{2}) (?P<numer>([0-9]{3} ){2}[0-9]{3})$", tekst)
if wynik:
    print(f"Dopasowano numer telefonu: +{wynik.group('kierunek')} {wynik.group('numer')}")
else:
    print("Nie dopasowano numeru telefonu")


print("\n\n##### ZADANIE 4 #####")

tekst = "13/10/1995"
wynik = re.match(r"^(?P<dni>[0-3]?[0-9]) ?[/,] ?(?P<miesiąc>[0-1]?[0-9]) ?[/,](?P<rok>[0-2][0-9]{0,3})$", tekst)
if wynik:
    print(f"Dopasowano datę: {wynik.group('dni')}-{wynik.group('miesiąc')}-{wynik.group('rok')}")
else:
    print("Nie dopasowano daty")


print("\n\n##### ZADANIE 5 #####")

tekst = r" Hello world! "
tekst = tekst.strip()
lista = re.findall(r"\S+", tekst)
print("lista <" + " ".join(lista) + ">")


print("\n\n##### ZADANIE 6 #####")

tekst = r" f  f 2.0 mp 3"
wynik = re.search(r"[0-9]+\.[0-9]+", tekst)
if wynik:
    print(f"Znaleziono: {wynik.group()}")
else:
    print("Nie znaleziono liczby zmiennoprzecinkowej")


print("\n\n##### ZADANIE 7 #####")

tekst = r"4:38 PM"
wynik = re.match(r"^(?P<godzina>[0-1]?[0-9]):(?P<minuta>[0-5][0-9]) (?P<dzień>[AP]M)", tekst)
if wynik:
    print(f"Dopasowano godzinę: {wynik.group('godzina')}:{wynik.group('minuta')} {wynik.group('dzień')}")
else:
    print("Nie dopasowano daty")


print("\n\n##### ZADANIE 8 #####")

tekst = r"https://xyz.abc.pl"
wynik = re.match(r"^(?P<protokół>http[s])?://(?P<witryna>[a-zA-Z0-9-]+\.)+(?P<strona>[a-z]{1,}(?<!\.))$", tekst)
if wynik:
    print(f"Dopasowano!")
    print(f"Protokół: {wynik.group('protokół')}")
    print(f"Witryna: {wynik.group('witryna')}")
    print(f"Strona: {wynik.group('strona')}")
else:
    print("Nie dopasowano")


print("\n\n##### ZADANIE 9 #####")

tekst = "192.168.0.4"
wzorzec = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})$"
wynik = re.match(wzorzec, tekst)
if wynik:
    print("Dopasowano adres IP:", wynik.group())
else:
    print("Nie dopasowano adresu IP")


print("\n\n##### ZADANIE 10 #####")

tekst = r"100.99 PLN"
wynik = re.match(r"^(?P<monety>[0-9]+\.)(?P<grosze>[0-9]{2}) (?P<waluta>[A-Za-z]+)$", tekst)
if wynik:
    print(f"Dopasowano kwotę: {wynik.group('monety')}{wynik.group('grosze')} {wynik.group('waluta')}")
else:
    print("Nie dopasowano kwoty")
