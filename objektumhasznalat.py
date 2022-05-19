# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int            :
        return self.a + self.b + self.c
    
haromszog = []
file = open('haromszog.txt','r')
file.readline()

for i in file:
    haromszog.append(i.strip().split('*'))
print(haromszog)

#hozz letre minden sorból egy Haromszog típusú objektumot
#Metódusa segitsegevel ird ki hogy a szamok  haromszoget alkotnak-e
for i in file:
    Egyharomszog = Haromszog(i)
    print(Egyharomszog.haromszoge())
    print(Egyharomszog.kerulet())    

