import random
class Kerdes():
    def __init__(self,sorszam,tipus,helyes,szoveg):
        self.sorszam = sorszam
        self.tipus = tipus
        self.helyes = helyes
        self.szoveg = szoveg
class Valasz():
    def __init__(self,sorszam,id,valasz):
        self.sorszam = sorszam
        self.id = id
        self.valasz = valasz

kerdes = []
valasz = []
file = open("kerdesek.csv", encoding="utf-8")
fajl = open("valaszok.csv", encoding="utf-8")
adat1 = file.readline().strip()
adat2 = fajl.readline().strip()

while adat1 != "":
    adat1 = adat1.split(";")
    adat1[0] = int(adat1[0])
    kerdes.append(Kerdes(adat1[0],adat1[1],adat1[2],adat1[3])) 
    adat1 = file.readline().strip()

while adat2 != "":
    adat2 = adat2.split(";")
    adat2[0] = int(adat2[0])
    valasz.append(Valasz(adat2[0],adat2[1],adat2[2])) 
    adat2 = file.readline().strip()

be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(t)/2)}): "))
while be1 > len(kerdes)/2:
    be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(t)/2)}): "))
szamlalo1 = 0
szamlalo2 = 0

for i in range(be1):
    veletlen = random.choice(kerdes)
    

