class kerdes():
    def __init__(self,sorszam,tipus,helyes,szoveg):
        self.sorszam = sorszam
        self.tipus = tipus
        self.helyes = helyes
        self.szoveg = szoveg
class valasz():
    def __init__(self,sorszam,id,valasz):
        self.sorszam = sorszam
        self.id = id
        self.valasz = valasz

t = []
t1 = []
file = open("kerdesek.csv", encoding="utf-8")
fajl = open("valaszok.csv", encoding="utf-8")
adat1 = file.readline().strip()
adat2 = fajl.readline().strip()

while adat1 != "":
    adat1 = adat1.split(";")
    adat1[0] = int(adat1[0])
    t.append(kerdes(adat1[0],adat1[1],adat1[2],adat1[3])) 
    adat1 = file.readline().strip()

while adat2 != "":
    adat2 = adat2.split(";")
    adat2[0] = int(adat2[0])
    t1.append(valasz(adat2[0],adat2[1],adat2[2])) 
    adat2 = file.readline().strip()

be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(t)/2)}): "))
while be1 > len(t)/2:
    be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(t)/2)}): "))
