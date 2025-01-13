class Match:
    def __init__(self, wzor, tekst, start):
        self.wzor = wzor
        self.tekst = tekst
        self.start_pos = start
        self.end_pos = start + len(wzor)
    
    def group(self):
        return self.wzor

    def start(self):
        return self.start_pos

    def end(self):
        return self.end_pos

    def span(self):
        return (self.start_pos, self.end_pos)

class Re:
    @staticmethod
    def match(wzor, tekst):
        if len(tekst) < len(wzor):
            return False

        if tekst[:len(wzor)] == wzor:
            return True
        return False

    @staticmethod
    def fullmatch(wzor, tekst):
        if len(tekst) != len(wzor):
            return None
        if tekst == wzor:
            return Match(wzor, tekst, 0)
        return None

    @staticmethod
    def search(wzor, tekst, flagi):
        if flagi and "IGNORECASE" in flagi:
            wzor = wzor.lower()
            tekst = tekst.lower()
        if len(tekst) < len(wzor):
            return None
        
        for i in range(len(tekst) - len(wzor) + 1):
            if tekst[i:i + len(wzor)] == wzor:
                return Match(wzor, tekst, i)
        return None
    
    @staticmethod
    def findall(wzor, tekst):
        dopasowania = []
        if len(tekst) < len(wzor):
            return dopasowania
        
        for i in range(len(tekst) - len(wzor) + 1):
            if tekst[i:i + len(wzor)] == wzor:
                dopasowania.append(wzor)

        return dopasowania

    @staticmethod
    def sub(wzor, zmiana, tekst):
        NowyTekst = ""
        i = 0
        
        while i <= len(tekst) - len(wzor):
            if tekst[i:i + len(wzor)] == wzor:
                NowyTekst += zmiana
                i += len(wzor)
            else:
                NowyTekst += tekst[i]
                i += 1
        
        NowyTekst += tekst[i:]
        return NowyTekst

    @staticmethod
    def split(wzor, tekst):
        result = []
        i = 0
        while i <= len(tekst):
            pos = tekst.find(wzor, i)
            if pos == -1:
                result.append(tekst[i:])
                break
            result.append(tekst[i:pos])
            i = pos + len(wzor)
        return result
    
print("tekst = 'Witaj świecie, witaj wszechświecie, witaj multiświecie!'\n")
tekst = "Witaj świecie, witaj wszechświecie, witaj multiświecie!"

print("Re.match('Witaj', tekst)")
print(f"match: {Re.match('Witaj', tekst)}\n")
print("Re.fullmatch(tekst, tekst)")
dopasowanie = Re.fullmatch(tekst, tekst)
print(f"fullmatch: {dopasowanie.group() if dopasowanie else 'Brak dopasowania'}\n")

print("Re.search('świecie', tekst, flagi=None")
dopasowanie = Re.search("świecie", tekst, flagi=None)
if dopasowanie:
    print(f"search: {dopasowanie.group()}, start: {dopasowanie.start()}, end: {dopasowanie.end()}, span: {dopasowanie.span()}\n")

print("Re.findall('witaj', tekst)")
print(f"findall: {Re.findall('witaj', tekst)}\n")

print("Re.sub('witaj', 'Cześć', tekst)")
print(f"sub: {Re.sub('witaj', 'Cześć', tekst)}\n")  

print("Re.split(',', tekst)")
print(f"split: {Re.split(',', tekst)}\n")

