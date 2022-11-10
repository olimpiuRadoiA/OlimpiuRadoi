version = '0.4.005'

class Oras():
    def __init__(self, ordX='', ordY='', nume='', judet='', auto='', populatie='', regiune=''):
        self.ordX = ordX
        self.ordY = ordY
        self.nume = nume
        self.judet = judet
        self.auto = auto
        self.populatie = populatie
        self.regiune = regiune
        
    def __str__(self):
        return self.ordX  +  self.ordY  +  self.nume  +  self.judet  +  self.auto  +  self.populatie  +   self.regiune
        
    def getOrdX(self):
        return self.ordX
    
    def getOrdY(self):
        return self.ordY
    
    def getNume(self):
        return self.nume
    
    def getJudet(self):
        return self.judet
    
    def getAuto(self):
        return self.auto
    
    def getPopulatie(self):
        return self.populatie
    
    def getRegiune(self):
        return self.regiune

def loadFile(file):
    f = open(file,'r')
    arr = []
    for line in f:
        
        latitudine = line[0:line.index(',')]  # aici obtin literele de la poz [0] pana inainte de pozitia primei , gasite
        line = line[line.index(',')+1:] # mai sus am obtinut ce doream deci tre sa sterg totuil pana la prima , inclisv
        
        
        longitudine = line[0:line.index(',')]
        line = line[line.index(',')+1:]
        
        
        oras = line[0:line.index(',')]
        line = line[line.index(',')+1:]
       
        
        judet = line[0:line.index(',')] 
        line = line[line.index(',')+1:]
       
        
        judetAuto = line[0:line.index(',')]
        line = line[line.index(',')+1:]
       
        
        populatie = line[0:line.index(',')]
        line = line[line.index(',')+1:]
        
        regiune = line[0:]
       
        arr.append(Oras(latitudine, longitudine, oras, judet, judetAuto, populatie, regiune))
                   
    f.close()
    
    return arr

arr = loadFile("orase1.csv")
print("am incarcat", len(arr), "orase")

cautOras = "Cugir"
for i in range (0,len(arr)):
    if arr[i].nume == cautOras:
        print("l-am gasit", arr[i].nume,arr[i].populatie)
        
        