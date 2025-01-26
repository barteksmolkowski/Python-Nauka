import datetime
print(f"datetime.date -> {datetime.date(2025, 12, 5)}")
print(f"datetime.time -> {datetime.time(12, 30, 5)}")

data = datetime.datetime.now()
print(f"data: {data}\n")
print("& -> %")
print(data.strftime("Year(&Y &y): %Y %y"))
print(data.strftime("Month(&m): %m"))
print(data.strftime("Day(&d): %d"))
print(data.strftime("Hour(&H &h): %H %h"))
print(data.strftime("Minutes(&M): %M"))
print(data.strftime("Second(&S): %S"))


print(data.strftime("razem: %D\n\n"))

def PokazGodzine():
    teraz = datetime.datetime.now()
    
    LiczbaGodzin = teraz.hour
    minuta = teraz.minute
    
    godzina = "PM" if LiczbaGodzin >= 12 else "AM"
    
    LiczbaGodzin = LiczbaGodzin % 12 or 12
    
    print(f"Godzina: {LiczbaGodzin}:{minuta:02d} {godzina}")

PokazGodzine()
