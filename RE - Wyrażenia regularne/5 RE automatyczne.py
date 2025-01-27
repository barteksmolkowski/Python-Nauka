import re

def dodajRE(slowo):
    slownik = {
        "a": "aqszQASZ", "ą": "ąqśżQĄŚŻ", "b": "bvghVBGH",
        "c": "cxdfXCDF", "ć": "ćxdfĆXDF", "d": "dfvgbDFVGB",
        "e": "erwsdEWRS", "ę": "ęerwsĘEWS", "f": "fgbhfFGHF",
        "g": "ghbnmGHBNM", "h": "hjnbvHJNBF", "i": "ikjloIKJLO",
        "j": "jknmMJN,LOI", "k": "klmioJKLIO", "l": "łóolŁOIO",
        "m": "mnkJLMNKM", "n": "nbghmNBHM", "ń": "ńbnKMŃBNK", 
        "o": "opikpOPIKP", "ó": "óopikÓOPIK", "p": "pól;pPOL;:>", 
        "r": "rtfgbRTFGB", "s": "asdxsASDXS", "ś": "śasdxŚASDX", 
        "t": "tyhgrTYHGR", "u": "uyjkiUYJKI", "w": "wqazwWQAZW",
        "x": "xcvbXCVB", "y": "ytguhYTGUE", "z": "zxcvZXC", 
        "ź": "źxcvŹXCV", "ż": "żxcvŻXCV"
    }

    nSlowo = ""
    
    for i, litera in enumerate(slowo):
        if litera.lower() in slownik:
            if 0 < i < len(slowo):
                nSlowo += f"[{slownik[litera.lower()]}][A-Za-z]*"
            else:
                nSlowo += f"[{slownik[litera.lower()]}?]"
        else:
            nSlowo += litera
    
    return f"^[A-Za-z]?{nSlowo}[A-Za-z]?$"

print(dodajRE("samochodzik"))

import re

randomowe_slowa = ["bartek", "kwiat", "kawa", "samtochtoeedtzik", "samochód"]

regex = r"^[A-Za-z]?[asdxsASDXS?][aqszQASZ][A-Za-z]*[mnkJLMNKM][A-Za-z]*[opikpOPIKP][A-Za-z]*[cxdfXCDF][A-Za-z]*[hjnbvHJNBF][A-Za-z]*[opikpOPIKP][A-Za-z]*[dfvgbDFVGB][A-Za-z]*[zxcvZXC][A-Za-z]*[ikjloIKJLO][A-Za-z]*[klmioJKLIO][A-Za-z]*[A-Za-z]?$"

pasujace_slowa = []

for slowo in randomowe_slowa:
    if re.fullmatch(regex, slowo):
        pasujace_slowa.append(slowo)

print("Słowa pasujące do wyrażenia regularnego:")
print(pasujace_slowa)

