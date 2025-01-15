import re

wzor = r"bartek" # rel
wzor2 = r"programowania" 
tekst = r"zdanie: bartek uczy się programowania . bartek"

print(re.match(wzor, tekst))
if re.match((f".*{wzor}.*"), tekst):#   MATCH
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.search(wzor, tekst):#    SEARCH
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

print(re.findall(wzor, tekst))#    FINDALL

dopasowanie = re.search(wzor, tekst)
if dopasowanie:#                        FUNKCJE Z SEARCH:
    print(dopasowanie.group())#         GROUP
    print(dopasowanie.start())#         START
    print(dopasowanie.end())#           END
    print(dopasowanie.span())#          SPAN

print(f"tekst przed zamianą: {tekst}")
tekst2 = re.sub(wzor2, r"matematyki", tekst)
print(f"tekst po zamianie: {tekst2}")