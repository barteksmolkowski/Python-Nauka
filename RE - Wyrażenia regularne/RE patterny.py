import re

# Pattern 1: Zaczyna się na 'B' i ma co najmniej 1 dodatkowy znak
pattern1 = r"B."
print(f"Pattern: {pattern1} - Dopasowuje tekst zaczynający się na 'B', a potem dowolny jeden znak.")
if re.match(pattern1, "Bartek"):
    print("Dopasowano: 'Bartek'")
else:
    print("Nie dopasowano: 'Bartek'")

# Pattern 2: Dokładnie 6-znakowy wyraz zaczynający się na 'b', kończący na 'k'
pattern2 = r"^b....k$"
print(f"\nPattern: {pattern2} - Dokładnie 6 znaków, zaczyna się na 'b', kończy na 'k'.")
if re.match(pattern2, "bartek"):
    print("Dopasowano: 'bartek'")
else:
    print("Nie dopasowano: 'bartek'")

# Pattern 3: Wyraz zaczynający się na 'S' lub 's', następnie dowolne 3 znaki, 'a' i '!'
pattern3 = r"^[Ss]...[a][!]$"
print(f"\nPattern: {pattern3} - Zaczyna się na 'S' lub 's', dowolne 3 znaki, 'a', i kończy się '!'.")
if re.match(pattern3, "Siema!"):
    print("Dopasowano: 'Siema!'")
else:
    print("Nie dopasowano: 'Siema!'")

# Pattern 4: Tekst zaczynający się od "Litera: " i dowolną literę (a-zA-Z)
pattern4 = r"^[Ll]itera: [a-zA-Z]"
print(f"\nPattern: {pattern4} - Zaczyna się na 'Litera: ', po czym występuje dowolna litera.")
if re.match(pattern4, "litera: F"):
    print("Dopasowano: 'litera: F'")
else:
    print("Nie dopasowano: 'litera: F'")

# Pattern 5: "Nie Litera: " + dowolny znak niebędący literą
pattern5 = r"^[Nn]ie [Ll]itera: [^a-zA-Z]"
print(f"\nPattern: {pattern5} - Zaczyna się na 'Nie Litera: ', po czym występuje znak niebędący literą.")
if re.match(pattern5, "nie Litera: 3"):
    print("Dopasowano: 'nie Litera: 3'")
else:
    print("Nie dopasowano: 'nie Litera: 3'")

# Pattern 6: "Nie Duży znak: " + mała litera
pattern6 = r"^[Nn]ie [Dd]u[zźż]y znak: [a-z]$"
print(f"\nPattern: {pattern6} - Zaczyna się na 'Nie Duży znak: ', po czym mała litera.")
if re.match(pattern6, "nie Duzy znak: b"):
    print("Dopasowano: 'nie Duzy znak: b'")
else:
    print("Nie dopasowano: 'nie Duzy znak: b'")

# Pattern 7: Rok + "-", "=", lub "_", a potem liczby 20xx (30 maksymalnie)
pattern7 = r"^[Rr]ok [-_=] 20[0-3][0-9][?!.]"
print(f"\nPattern: {pattern7} - 'Rok -', 'Rok =', lub 'Rok _', po czym 20xx (30 maksymalnie). Musi kończyć się '?', '!' lub '.'.")
if re.match(pattern7, "rok = 2024?"):
    print("Dopasowano: 'rok = 2024?'")
else:
    print("Nie dopasowano: 'rok = 2024?'")

# Pattern 8: Rok + separator i dowolna liczba zakończona znakiem "!" lub "?"
pattern8 = r"^[Rr]ok[=:-] [0-9]*[!?]"
print(f"\nPattern: {pattern8} - 'Rok=', 'Rok:', 'Rok-', po czym dowolna liczba zakończona '!' lub '?'.")
if re.match(pattern8, "Rok: 193?"):
    print("Dopasowano: 'Rok: 193?'")
else:
    print("Nie dopasowano: 'Rok: 193?'")

if re.match(r"^[A-Z][a-z]+$", "Bartek"): # plus mówi że musi wystąpić co najmniej raz
    print("dopasowano")
else:
    print("nie dopasowano")

if re.match(r"^[A-Z][a-z]*?[0-9]$", "Bartek4"):# ? mówi że możeWystąpićZnakPo lewo ale nie musi
    print("dopasowano")
else:
    print("nie dopasowano")

if re.match(r"^[A-Z][a-z]{3,5}$", "Bartek"):#
    print("dopasowano")
else:
    print("nie dopasowano")

if re.match(r"^[Rr]?o?k? ?[-:=;]? ?[>]? ?[0-9]{0,4}$", "rok-> 999"):
    print("dopasowano")
else:
    print("nie dopasowano")

if re.match(r"^[A-Za-z][a-z]*?.[A-Za-z][a-z]*?@[a-z]+.[a-z]{3,}$", "Xyz.Abc@gmail.com"):
    print("dopasowano")
else:
    print("nie dopasowano")

wynik =  re.match(r"^(Witam) (z) (tej) (strony) (Bartek)$", "Witam z tej strony Bartek")

if wynik:
    print("Dopasowano")
    print(wynik.group(1))
    print(wynik.groups())

wynik = re.findall(r"[JjIi]abłe?k[oa]", "Zebrałem jabłko jabłka Iabłko")

if wynik:
    print(f"Jabłek jest: {len(wynik)}")
else:
    print("Nie znaleziono jabłek!")

wynik = re.match(r"^(?P<tekst>[A-Za-z]+) ?(?P<myślnik>[-:=][>=]?) ?(?P<imię>[A-Za-z][a-z]+) (?P<nazwisko>[A-Za-z][a-z]+) (?P<lat>[0-9]{1,3})", "Zdanie => Bartek Kowalski 123")

if wynik:
    print(f"tekst: {wynik.group('tekst')}\n"
          f"myślnik: {wynik.group('myślnik')}\n"
          f"imię: {wynik.group('imię')}\n"
          f"nazwisko: {wynik.group('nazwisko')}\n"
          f"lat: {wynik.group('lat')}")
else:
    print("Nie dopasowano")

wynik = re.match(r"^(?:[Ll]at) ?(?P<myślnik>[-:=][>]?)? ?(?P<lat>[0-9])+ (!|.)$", "lat - 33 b")
if wynik:
    print(f"myślnik: {wynik.group('myślnik')}")
    print(f"lat: {wynik.group('lat')}")


wynik = re.match(r"(?P<imię>[A-Z][A-Za-z0-9]{3,}) ?. ?(?P<nazwisko>[A-Z][A-Za-z0-9]{5,})@(?P<właściciel>[a-z]+).(?P<domena>[a-z]{3,}+)", "Bart3k.Smolk0wski@gmail.com")

if wynik:
    print(f"użytkownik: {wynik.group("imię")} {wynik.group("nazwisko")}")
    print(f"Założono na stronie: {wynik.group("właściciel")}.{wynik.group("domena")}")


wynik = re.match(r"owoce => (?P<owoce>(truskawka|borówka|ananas)(, (truskawka|borówka|ananas))*)", "owoce => truskawka, borówka, ananas, borówka")

def StworzSlownik(tablica):
    slownik = {}
    for i in range(len(tablica)):
        if tablica[i] not in slownik:
            slownik[tablica[i]] = 0
        slownik[tablica[i]] += 1
    return slownik

if wynik:
    lista = wynik.group("owoce").split()
    lista = [owoce.replace(",", "") for owoce in lista]
    slownik = StworzSlownik(lista)
    print(f"Znaleziono owoce: {slownik}")
else:
    print("Nie dopasowano.")

