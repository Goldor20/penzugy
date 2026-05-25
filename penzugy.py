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
    adat2 = fajl.readline().strip()

be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(kerdes)/2)}): "))
while be1 > len(kerdes)/2:
    be1 = int(input(f"Hány kört szeretne játszani (max: {round(len(kerdes)/2)}): "))
szamlalo1 = 0
szamlalo2 = 0

for i in range(be1):
    veletlen = random.choice(kerdes)
    if veletlen.tipus == "Y":
        print(f"DUPLAPONTOS KÉRDÉS!!!")
        print(f"{i+1}. Kérdés: {veletlen.szoveg}")
    else:
        print(f"{i+1}. Kérdés: {veletlen.szoveg}")
    for n in range(2):
        print(f"--- {n+1}. játékos válasza ---")
        
        if veletlen.tipus == "Y":
            be2 = input("Y/N: ")
            be2 = be2.upper()
            if be2 == veletlen.helyes:
                if n == 0: szamlalo1 += 2
                else: szamlalo2 += 2
        
        elif veletlen.tipus == "F":
            print("Választható lehetőségek:")
            for v in valasz:
                if v.sorszam == veletlen.sorszam:
                    print(f"{v.id}) {v.valasz}")
            
            be2 = input("Írd be a választ jelentő betűt: ")
            be2 = be2.upper()
            if be2 == veletlen.helyes:
                if n == 0:
                    szamlalo1 += 1
                else:
                    szamlalo2 += 1

    print(f"Jelenlegi állás: {szamlalo1} - {szamlalo2}")
