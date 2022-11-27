import os
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

def menu():
    print("1. RO")
    
        
OP_EXIT = '10'

op = 0

while op != OP_EXIT:
    
    op = input("Introduceti  optiunea dorita pentru a continua in limba romana RO sau limba engleza EN: ")
    
    print("RO")
    print("EN")
    print ("10. EXIT")
   
    
    
    
    
    if op == "RO":
        
        
        
        OP_EXIT1 = "10"
        while op != OP_EXIT1:
            os.system('cls')
        
            menuOption01 = "1.Citire fisier"
            menuOption02 = "2.Cautare oras"
            menuOption10 = "10.Iesire"
            print ("Ati ales limba romana, va rugam continuati")
            print (menuOption01)
            print (menuOption02)
            print (menuOption10)
        
            op = input("Introduceti  optiunea dorita 1.Citire fisier SAU 2.Cautare oras: ")
        
            if op == '1':
            
                arr = loadFile("orase1.csv")
                print("am incarcat", len(arr), "orase")
                input("Apasati enter pentru a reveni la meniu")
    
            if op == '2':
                cautOras = input("intyroduceti Orasul cautat: ")
                for i in range (0,len(arr)):
                    if arr[i].nume == cautOras:
                        print("l-am gasit: ", arr[i].nume,arr[i].populatie,arr[i].judet,arr[i].auto, arr[i].regiune)
                input("Apasati enter pentru a reveni la meniu")
            
    if op =="EN":
        
        OP_EXIT2 = "10"
        while op != OP_EXIT2:
            os.system('cls')
        
            menuOption01 = "1.Load file"
            menuOption02 = "2.Search"
            menuOption10 = "10.Exit"
            print ("you chose English, please continue")
            print (menuOption01)
            print (menuOption02)
            print (menuOption10)
        
            op = input("Choose option 1. Read file OR 2. Search city: ")
        
            if op == '1':
            
                arr = loadFile("orase1.csv")
                print("have", len(arr), "citys")
                input("Press Enter to go back to Menu")
    
            if op == '2':
                cautOras = input("What is the city that you search: ")
                for i in range (0,len(arr)):
                    if arr[i].nume == cautOras:
                        print("find it: ", arr[i].nume,arr[i].populatie,arr[i].judet,arr[i].auto, arr[i].regiune)
                input("Press Enter to go back to Menu")
                