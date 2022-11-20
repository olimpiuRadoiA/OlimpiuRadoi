import os

def indexOf(line, deCautat):
    poz = -1
    try:
        poz = line.index(deCautat)
    except:
        poz = -1
    return poz

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
        
        latitudine = line[0:line.index(',')]
        line = line[line.index(',')+1:]
        
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

class Menu:
    OP_EXIT = '9'

    UNKNOWN_LANGUAGE = "unknown_language"

    op1     = UNKNOWN_LANGUAGE
    op2     = UNKNOWN_LANGUAGE
    op3     = UNKNOWN_LANGUAGE
    op4     = UNKNOWN_LANGUAGE
    op5     = UNKNOWN_LANGUAGE
    opExit  = UNKNOWN_LANGUAGE

    
    def load(self, language):
        f = open('menu-' + language +'.ini','r')
        for line in f:
            if indexOf(line,'menuOption01')>-1:
                self.op1 = line[line.index('=')+1:len(line)-1]
            if indexOf(line, 'menuOption02')>-1:
                self.op2 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption03')>-1:
                self.op3 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption04')>-1:
                self.op4 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption05')>-1:
                self.op5 = line[line.index('=')+1:len(line)-1]     
            if indexOf(line,'menuExit')>-1:
                self.opExit = line[line.index('=')+1:len(line)-1]
            
        f.close()
    
    def readValue(self, msg):
        return input(msg + ' ')
        
class Messages:

    msgChooseOption = "Alegeti Optiunea "
    msgEnterLanguage = "Introduceti Limba de Afisare "
    msgInLatitudine = "Introduceti Latitudinea"
    msgInNLongitudine = "Introduceti Longitudine"
    msgInOras = "Introduceti Nume Oras"
    msgInjudet = "Introduceti Nume Judet"
    msgInJudetAuto = "Introduceti Abreviere Judet AUTO"
    msgInPopulatie = "Introduceti Populatia Orasului"
    msgInRegiune = "Introduceti Regiunea din care face parte Orasul"
    
    
    
    def load(self, language):
        f = open("messages-" + language + ".ini",'r')
        for line in f:
            if indexOf(line, "menuOption01") > -1:
                self.msgChooseOption = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "menuOption02") > -1:
                self.msgEnterLanguage = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInLatitudine") > -1:
                self.msgInLatitudine = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInNLongitudine") > -1:
                self.msgInNLongitudine = line[line.index('=') + 1:len(line)-1] 
            if indexOf(line, "msgInOras") > -1:
                self.msgInOras = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInjudet") > -1:
                self.msgInjudet = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInJudetAuto") > -1:
                self.msgInJudetAuto = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInPopulatie") > -1:
                self.msgInPopulatie = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInRegiune") > -1:
                self.msgInRegiune = line[line.index('=') + 1:len(line)-1]
            if indexOf(line, "msgInNouaPopulatie") > -1:
                self.msgInNouaPopulatie = line[line.index('=') + 1:len(line)-1]
    
        f.close()
    
language = "ro"
arr = []

messages = Messages()
messages.load(language)

menu = Menu()
menu.load(language)

op = 0

while op != menu.OP_EXIT:
    os.system("cls")
        
    print(menu.op1 + language)
    print(menu.op2)
    print(menu.op3)
    print(menu.op4)
    print(menu.op5)
    print(menu.opExit)
        
    op = input(messages.msgChooseOption)
        
    if op == '1':
        language = input(messages.msgEnterLanguage)
        menu.load(language)
        messages.load(language)
        
        
    if op == '2':
        arr = loadFile("orase1.csv")
        print("am incarcat", len(arr), "orase")
        input("Apasati enter pentru a reveni la meniu")
        
    if op == '3':
        cautOras = input("introduceti Orasul cautat: ")
        for i in range (0,len(arr)):
            if arr[i].nume == cautOras:
                print("l-am gasit: ", arr[i].nume,arr[i].populatie,arr[i].judet,arr[i].auto, arr[i].regiune)
        input("Apasati enter pentru a reveni la meniu")        
        
    if op == '4':
        latitudine = menu.readValue(messages.msgInLatitudine)
        longitudine = menu.readValue(messages.msgInNLongitudine)
        nume = menu.readValue(messages.msgInOras)
        judet = menu.readValue(messages.msgInjudet)
        judetAuto = menu.readValue(messages.msgInJudetAuto)
        populatie = menu.readValue(messages.msgInPopulatie)
        regiune = menu.readValue(messages.msgInRegiune)
    
        
        try:
            orasNou = Oras(latitudine, longitudine, nume, judet, judetAuto, populatie, regiune)
            arr.append(orasNou)
            isDirty = True
        except TypeError as e:
            print(e)
        input("Apasati enter pentru a reveni la meniu")
        
    if op == '5':
        
        nume = menu.readValue(messages.msgInOras)
        populatie = menu.readValue(messages.msgInNouaPopulatie)
        
        
        schimbareOras = nume
        for i in range (0, len(arr)):
            if arr[i].nume == schimbareOras:
                arr[i].populatie = populatie
        schimbareOras = Oras(nume, populatie)
        