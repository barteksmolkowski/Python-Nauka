import datetime
import locale
import pytz

print("Zadanie 1")
def RRRRMMDDHHMMS():
    czas = datetime.datetime.now()
    return f"{czas.year}-{czas.month:02}-{czas.day:02}-{czas.hour:02}-{czas.minute:02}-{czas.second:02}"
print(RRRRMMDDHHMMS())
print("\n")

print("Zadanie 2")
def RoznicaDat(data1: tuple[int, int, int, int, int, int], data2: tuple[int, int, int, int, int, int]):
    dData = {}
    for i in range(0, 6):
        dData[i] = abs(data1[i] - data2[i])
    dRoznica = (dData[0], dData[1], dData[2], dData[3], dData[4], dData[5])
    print(f"{data1} - {data2} = {dRoznica}")
    return dRoznica
print(RoznicaDat((1994, 5, 25, 13, 50, 52), (2008, 1, 14, 6, 31, 9)))
print("\n")

print("Zadanie 3")
def FormatujData(data: tuple[int, int, int, int, int, int]) -> None:
    locale.setlocale(locale.LC_TIME, "pl_PL")
    Dzien = datetime.datetime(data[0], data[1], data[2], data[3], data[4], data[5])
    print(Dzien.strftime("%d %B %Y, %H:%M:%S"))
    print(Dzien.strftime("%A, %d %b %Y"))
    print(Dzien.strftime("%d/%m/%Y %H:%M:%S"))
FormatujData((1994, 8, 25, 13, 50, 52))
print("\n")

print("Zadanie 4")
def DodajDate(data1: tuple[int, int, int, int, int, int]):
    data1 = datetime.datetime(data1[0], data1[1], data1[2], data1[3], data1[4], data1[5])
    data2 = data1 + datetime.timedelta(days=5, hours=20, minutes=30)
    print(data2)
DodajDate((1994, 8, 25, 13, 50, 52))
print("\n")

print("Zadanie 5")
def UrodzinyData(dataUrodzenia: str):
    rok, miesiac, dzien = map(int, dataUrodzenia.split("-"))
    data_urodzenia = datetime.datetime(rok, miesiac, dzien)
    aktualData = datetime.datetime.now()

    # rok
    wiek = aktualData.year - data_urodzenia.year
    if (aktualData.month, aktualData.day) < (data_urodzenia.month, data_urodzenia.day):
        wiek -= 1

    # miesiąc
    if aktualData.month >= data_urodzenia.month:
        miesiac = aktualData.month - data_urodzenia.month
    else:
        miesiac = aktualData.month + 12 - data_urodzenia.month

    # dni
    if aktualData.day >= data_urodzenia.day:
        dni = aktualData.day - data_urodzenia.day
    else:
        # Zmniejszamy miesiąc o 1, żeby uzyskać dni w poprzednim miesiącu
        poprzedni_miesiac = (aktualData.replace(day=1) - datetime.timedelta(days=1))
        dni = (poprzedni_miesiac.day + aktualData.day - data_urodzenia.day)

    print(f"Masz {wiek} lat, {miesiac} miesięcy i {dni} dni.")
UrodzinyData("2008-12-29")
print("\n")

print("Zadanie 6")
def Soboty():
    dzisiaj = datetime.datetime.now()
    dzienTyg = dzisiaj.weekday()

    DniWsteczDoSob = (dzienTyg - 5) % 7
    poprzedniaSob = dzisiaj - datetime.timedelta(days=DniWsteczDoSob)

    DniPrzodDoSob = dzienTyg % 7
    NastepnaSob = dzisiaj + datetime.timedelta(days=DniPrzodDoSob)

    print(f"Poprzednia sobota: {poprzedniaSob.strftime('%d.%m.%Y')}")
    print(f"Następna sobota: {NastepnaSob.strftime('%d.%m.%Y')}")
Soboty()
print("\n")

print("Zadanie 7")

def StrefyCzasowe()