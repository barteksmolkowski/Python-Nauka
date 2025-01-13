import re

# Pattern 1: Zaczyna się na 'B' i ma co najmniej 1 dodatkowy znak
pattern1 = "B."
print(f"Pattern: {pattern1} - Dopasowuje tekst zaczynający się na 'B', a potem dowolny jeden znak.")
if re.match(pattern1, "Bartek"):
    print("Dopasowano: 'Bartek'")
else:
    print("Nie dopasowano: 'Bartek'")

# Pattern 2: Dokładnie 6-znakowy wyraz zaczynający się na 'b', kończący na 'k'
pattern2 = "^b....k$"
print(f"\nPattern: {pattern2} - Dokładnie 6 znaków, zaczyna się na 'b', kończy na 'k'.")
if re.match(pattern2, "bartek"):
    print("Dopasowano: 'bartek'")
else:
    print("Nie dopasowano: 'bartek'")

# Pattern 3: Wyraz zaczynający się na 'S' lub 's', następnie dowolne 3 znaki, 'a' i '!'
pattern3 = "^[Ss]...[a][!]$"
print(f"\nPattern: {pattern3} - Zaczyna się na 'S' lub 's', dowolne 3 znaki, 'a', i kończy się '!'.")
if re.match(pattern3, "Siema!"):
    print("Dopasowano: 'Siema!'")
else:
    print("Nie dopasowano: 'Siema!'")

# Pattern 4: Tekst zaczynający się od "Litera: " i dowolną literę (a-zA-Z)
pattern4 = "^[Ll]itera: [a-zA-Z]"
print(f"\nPattern: {pattern4} - Zaczyna się na 'Litera: ', po czym występuje dowolna litera.")
if re.match(pattern4, "litera: F"):
    print("Dopasowano: 'litera: F'")
else:
    print("Nie dopasowano: 'litera: F'")

# Pattern 5: "Nie Litera: " + dowolny znak niebędący literą
pattern5 = "^[Nn]ie [Ll]itera: [^a-zA-Z]"
print(f"\nPattern: {pattern5} - Zaczyna się na 'Nie Litera: ', po czym występuje znak niebędący literą.")
if re.match(pattern5, "nie Litera: 3"):
    print("Dopasowano: 'nie Litera: 3'")
else:
    print("Nie dopasowano: 'nie Litera: 3'")

# Pattern 6: "Nie Duży znak: " + mała litera
pattern6 = "^[Nn]ie [Dd]u[zźż]y znak: [a-z]$"
print(f"\nPattern: {pattern6} - Zaczyna się na 'Nie Duży znak: ', po czym mała litera.")
if re.match(pattern6, "nie Duzy znak: b"):
    print("Dopasowano: 'nie Duzy znak: b'")
else:
    print("Nie dopasowano: 'nie Duzy znak: b'")

# Pattern 7: Rok + "-", "=", lub "_", a potem liczby 20xx (30 maksymalnie)
pattern7 = "^[Rr]ok [-_=] 20[0-3][0-9][?!.]"
print(f"\nPattern: {pattern7} - 'Rok -', 'Rok =', lub 'Rok _', po czym 20xx (30 maksymalnie). Musi kończyć się '?', '!' lub '.'.")
if re.match(pattern7, "rok = 2024?"):
    print("Dopasowano: 'rok = 2024?'")
else:
    print("Nie dopasowano: 'rok = 2024?'")

# Pattern 8: Rok + separator i dowolna liczba zakończona znakiem "!" lub "?"
pattern8 = "^[Rr]ok[=:-] [0-9]*[!?]"
print(f"\nPattern: {pattern8} - 'Rok=', 'Rok:', 'Rok-', po czym dowolna liczba zakończona '!' lub '?'.")
if re.match(pattern8, "Rok: 193?"):
    print("Dopasowano: 'Rok: 193?'")
else:
    print("Nie dopasowano: 'Rok: 193?'")

if re.match("^[A-Z][a-z]+$", "Bartek"): # plus mówi że musi wystąpić co najmniej raz
    print("dopasowano")
else:
    print("nie dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$", "Bartek"):
    print("dopasowano")
else:
    print("nie dopasowano")