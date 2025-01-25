import datetime

def RRRRMMDDHHMMS():
    czas = datetime.datetime.now()
    return f"{czas.year}-{czas.month:02}-{czas.day:02}-{czas.hour:02}-{czas.minute:02}-{czas.second:02}"

print(RRRRMMDDHHMMS())

def OdczytajDMR(data):
    return

def Różnica(data1, data2):
    OdczytajDate()