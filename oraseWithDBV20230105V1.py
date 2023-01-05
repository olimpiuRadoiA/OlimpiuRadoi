import os
from datetime import datetime
import mysql.connector



def indexOf(line, deCautat):
    poz = -1
    try:
        poz = line.index(deCautat)
    except:
        poz = -1
    return poz


class Oras():
    def __init__(self, ordX=0, ordY=0, nume='', judet='', auto='', populatie=0, regiune=''):
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
        return int(self.populatie)
    
    def getRegiune(self):
        return self.regiune
    
    def setNume(self, nume):            
        msg = self.validateNume(nume)
        if msg == "ok":
            if ord(nume[0]) >= ord('a') and ord(nume[0]) <= ord('z'):
                nume = "" + chr(ord(nume[0])-32) + nume[1:]                
            self.nume = nume
        else:
            raise TypeError(msg)
            
    def validateNume(self, nume):        
        msg = "ok"
        if len(nume) < 3:
            msg = "Numele trebuie sa aiba cel putin 3 caractere"
            
        return msg
    

def loadFile(file):
    f = open(file,'r')
    arr = []
    f.readline()
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
        
        if line[0:line.index(',')] == '':
            populatie = 0
        else:
            populatie = int(line[0:line.index(',')])
            line = line[line.index(',')+1:]
        
        regiune = line[0:]
       
        arr.append(Oras(latitudine, longitudine, oras, judet, judetAuto, populatie, regiune))
                   
    f.close()
    return arr

mydb = mysql.connector.connect ( host="localhost", port="3306", user="agendatelefonica", password="root1234", database ="agendatelefonica" )

22

windowsEndLine = '\n'

def write(f, line):
    f.write(line)
    
def writeLn(f, line):
    f.write(line + windowsEndLine)

def writeToFile(listaLiniiOrase, file):
    f = open(file, 'w')
    f.write('X,Y,Nume,JUDET,JUDET AUTO,POPULATIE(in2002),REGIUNE')
    f.write(str(listaLiniiOrase))
    f.close()
    
def saveNewInfoToFile(arr, file):
    f = open(file, 'w')
    
    
    i = 0
    n = len(arr)
    
    for city in arr:
        line = str(city.getOrdX()) + ',' + str(city.getOrdY()) + ',' + str(city.getNume()) + ',' + city.getJudet() + ',' + city.getAuto() + ',' + str(city.getPopulatie()) + ',' + city.getRegiune()
        
        if i < n-1 :
            write(f, line)
        else:
            writeLn(f, line)
        
        i = i + 1
    
    f.close()
    
class Menu:
    OP_EXIT = '0'

    UNKNOWN_LANGUAGE = "unknown_language"

    op01     = UNKNOWN_LANGUAGE
    op02     = UNKNOWN_LANGUAGE
    op03     = UNKNOWN_LANGUAGE
    op04     = UNKNOWN_LANGUAGE
    op05     = UNKNOWN_LANGUAGE
    op06     = UNKNOWN_LANGUAGE
    op07     = UNKNOWN_LANGUAGE 
    op09     = UNKNOWN_LANGUAGE
    op10     = UNKNOWN_LANGUAGE
    op11     = UNKNOWN_LANGUAGE
    op12     = UNKNOWN_LANGUAGE
    op13     = UNKNOWN_LANGUAGE
    op35     = UNKNOWN_LANGUAGE
    op20     = UNKNOWN_LANGUAGE
    op22     = UNKNOWN_LANGUAGE
    op23     = UNKNOWN_LANGUAGE
    op27     = UNKNOWN_LANGUAGE
    op29     = UNKNOWN_LANGUAGE
    op32     = UNKNOWN_LANGUAGE
    opExit   = UNKNOWN_LANGUAGE

    
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
            if indexOf(line,'menuOption06')>-1:
                self.op6 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption07')>-1:
                self.op7 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption09')>-1:
                self.op9 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption10')>-1:
                self.op10 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption11')>-1:
                self.op11 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption12')>-1:
                self.op12 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption13')>-1:
                self.op13 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption35')>-1:
                self.op35 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption20')>-1:
                self.op20 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption22')>-1:
                self.op22 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption23')>-1:
                self.op23 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption27')>-1:
                self.op27 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption29')>-1:
                self.op29 = line[line.index('=')+1:len(line)-1]
            if indexOf(line,'menuOption32')>-1:
                self.op32 = line[line.index('=')+1:len(line)-1]
                
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
        


os.chdir("Documents")
os.chdir("Python/20221115")


language = "ro"
arr = []

messages = Messages()
messages.load(language)

menu = Menu()
menu.load(language)

fisier = "orase.csv"

SCHIMBARE_LIMBA = '1'
INCARCARE_FISIER = '2'
CAUTARE_ORAS = '3'
ADAUGARE_ORAS = '4'
MODIFICARE_INFORMATII_ORAS = '5'
SALVARE_MODIFICARE_ORAS = '6'
CEL_MAI_MARE_ORAS_NR_LOCUITORI = '7'
STERGEREA_UNUI_ORAS_LEVEL01 = '9'
STERGEREA_UNUI_ORAS_LEVEL02 = '10'
SORTARE_ORASE_DECRESCATOR_IN_FUNCTIE_DE_POPULATIE = '11'
SORTARE_ORASE_DECRESCATOR_IN_FUNCTIE_DE_POPULATIE_V2 = '12'
AFISARE_ARR_INDIF_DE_SURSA_DIN_CARE_A_FOST_INCARCAT ='13'
AFISARE_INFO_DIN_BD ='35'
TRUNCATE_INFO_DIN_BD ='20'
INARCARE_INFO_DIN_BD_IN_ARR ='22'
STERGERE_ORAS_BD = '23'
AFISARE_ORAS_BD_POPULATIE_MAXIMA ='27'
STERGERE_ORAS_BD ='29'
AFISARE_INFO_FISIER = '32'

EXIT = '0'

isDirty = False

op = -1

while op != menu.OP_EXIT:
    os.system("cls")
        
    print(menu.op1 + language)
    print(menu.op2)
    print(menu.op3)
    print(menu.op4)
    print(menu.op5)
    if isDirty == True:
        print(menu.op6 + " *")    
    else:
        print(menu.op6)
    print(menu.op7)
    print(menu.op9)
    print(menu.op10)
    print(menu.op11)
    print(menu.op12)
    print(menu.op13)
    print(menu.op35)
    print(menu.op20)
    print(menu.op22)
    print(menu.op23)
    print(menu.op27)
    print(menu.op29)
    print(menu.op32)
    print(menu.opExit)
        
    op = input(messages.msgChooseOption)
        
    if op == SCHIMBARE_LIMBA:
        language = input(messages.msgEnterLanguage)
        menu.load(language)
        messages.load(language)
        
        
    if op == INCARCARE_FISIER:
        arr = loadFile(fisier)
        
        print("am incarcat", len(arr), "orase")
        
        
        cateOrase = len(arr)
        input("Apasati enter pentru a reveni la meniu")
        
    if op == CAUTARE_ORAS:
        cautOras = input("introduceti Orasul cautat: ")
        
                      
        for i in range (0,len(arr)):
            if arr[i].nume == cautOras:
                print("Orasul cautat")
                print("l-am gasit: ", arr[i].nume,arr[i].populatie,arr[i].judet,arr[i].auto, arr[i].regiune)
        
        
            
            
        input("Apasati enter pentru a reveni la meniu ")        
        
    if op == ADAUGARE_ORAS:
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
        
    if op == MODIFICARE_INFORMATII_ORAS:
        
        nume = menu.readValue(messages.msgInOras)
        populatie = menu.readValue(messages.msgInNouaPopulatie)
        
        
        schimbareOras = nume
        for i in range (0, len(arr)):
            if arr[i].nume == schimbareOras:
                arr[i].populatie = populatie
        schimbareOras = Oras(nume, populatie)
    
    if op == SALVARE_MODIFICARE_ORAS:
        if len(arr) == 0:
            print ("ERR")
        else: 
            saveNewInfoToFile(arr, fisier)
            isDirty = False
            print("SUCCES")
            
    if op == CEL_MAI_MARE_ORAS_NR_LOCUITORI:
        
        maxim = -1
        
        
        for i in range (0, len(arr)):
            if  arr[i].populatie > maxim:
                maxim = arr[i].populatie
        
        for i in range (0, len(arr)):
            if arr[i].populatie == maxim:
                print()
                print("Din punct de vedere al nr de locuitori, orasul ", arr[i].nume, "este cel mai mare si are ", arr[i].populatie, "locuitori")        
        
        print()
        input("Apasati enter pentru a reveni la meniu")
        

        
    
    if op == STERGEREA_UNUI_ORAS_LEVEL01: #O(n/2) ..ca memorie O(1)
        liniaOrasuluiDeSters = input("Care este orasul pe care doriti sa il stergeti?: ")
        poz = -1
        for i in range (0, cateOrase):
            if arr[i].nume == liniaOrasuluiDeSters:
                print(arr[i].nume)
                poz = i
        if poz == -1:
            print("nu a fost gasit")
        else:        
            for i in range (poz, cateOrase-1):
                arr[i] = arr[i+1]
                    
            cateOrase = cateOrase - 1
        
    #in acelasi timp eu am 26000 de orase
    if op == STERGEREA_UNUI_ORAS_LEVEL02: #O(n) timp ..ca memorie O(n)
        liniaOrasuluiDeSters = input("Care este orasul pe care doriti sa il stergeti?: ")
        aux= []
        for i in range (0, len(arr)):
            if arr[i].nume != liniaOrasuluiDeSters:
                aux.append(arr[i])
        arr.clear
        arr = aux
        
    if op == SORTARE_ORASE_DECRESCATOR_IN_FUNCTIE_DE_POPULATIE:
        startTime = datetime.now()
        aAparutOSchimbare = True
        while aAparutOSchimbare:
            aAparutOSchimbare = False
            for i in range (0,(len(arr)-1)):
            
                if arr[i].populatie > arr[i+1].populatie:
                    aux = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = aux
                    aAparutOSchimbare = True
        endTime = datetime.now()
        difTime = endTime - startTime
            
        print(difTime.total_seconds())
        input("Apasati enter pentru a reveni la meniu")
        
    if op == SORTARE_ORASE_DECRESCATOR_IN_FUNCTIE_DE_POPULATIE_V2:
        startTime = datetime.now()
        for i in range (0,(len(arr)-1)):
            for j in range (i+1,len(arr)):
                if arr[i].populatie > arr[j].populatie:
                    aux = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aux
        endTime = datetime.now()
        difTime = endTime - startTime
            
        print(difTime.total_seconds())
        
        input("Apasati enter pentru a reveni la meniu")
        
    if op == AFISARE_ARR_INDIF_DE_SURSA_DIN_CARE_A_FOST_INCARCAT:

        if len(arr) == 0:
            print ("Load the file first. What to insert ?")
        
        else: 
            for i in range (0,len(arr)):
                print(arr[i].ordX,arr[i].ordY,arr[i].nume,arr[i].populatie,arr[i].judet,arr[i].auto, arr[i].regiune)
        input("Apasati enter pentru a reveni la meniu")        
            
        
    if op == AFISARE_INFO_DIN_BD : #afisare orase din baza de date
        myCursor = mydb.cursor()

        myCursor.execute('SELECT * FROM orase') #select all
        oraseRecords = myCursor.fetchall()

        myCursor.close()
        

        #ce fac cu el : il parcurg si de data asta il afisez
        for record in oraseRecords:
            print(record)
        cuvinteRand=len(record)
        print(len(record),"nr cuvinte pe rand")
        print(record[0], "orase")
        nrTotalOrase = record[0]   
        print(nrTotalOrase)
        input("Apasati enter pentru a reveni la meniu")  
        
    if op == TRUNCATE_INFO_DIN_BD: 
        if len(arr) == 0:
            print ("Load the file first. WHat to insert ?")
        else: 
            myCursor = mydb.cursor()
            myCursor.execute("TRUNCATE orase")
            mydb.commit()
            myCursor.close()
            for i in range (0, len(arr)): #maxim de ineficienta dar merge
                myCursor = mydb.cursor()
                val = (arr[i].ordX, arr[i].ordY,arr[i].nume, arr[i].judet,arr[i].auto,arr[i].populatie,arr[i].regiune)
                sql = 'INSERT INTO orase (x,y,nume,judet,judetauto,populatie2002,regiune) VALUES (%s, %s, %s,%s, %s, %s, %s)'
                myCursor.execute(sql, val)
                mydb.commit()
                myCursor.close()
            
        input("Apasati enter pentru a reveni la meniu")
        
    if op ==INARCARE_INFO_DIN_BD_IN_ARR:   
        myCursor = mydb.cursor()

        myCursor.execute('SELECT * FROM orase')
        oraseRecords = myCursor.fetchall()
        

        myCursor.close()
        arr = []
        
        for record in oraseRecords:
            
    
            x = record[1]
              
            y = record[2]
             
            nume = record[3]
            
            judet = record[4]
            
            judetauto = record[5] 
           
            populatie2002 = record[6]
             
            regiune = record[7]
            
                    
            
            arr.append(Oras(x,y,nume,judet,judetauto,populatie2002,regiune))
          
        print("am incarcat",len(arr),"orase")   
        input("Apasati enter pentru a reveni la meniu")
        
        

    if op == STERGERE_ORAS_BD:
        if len(arr) == 0:
            print ("Load the file first. What to insert ?")
            
        else:
            orasulCautat = input("ce oras cautati?: ")
              
            myCursor = mydb.cursor()
            sql = "SELECT * FROM agendatelefonica.orase WHERE nume = '" + orasulCautat + "'"
            myCursor.execute(sql)
            myRecords = myCursor.fetchall()   
            myCursor.close()
            
            
            for record in myRecords:
                
                print(record[3])
                   
        input("Apasati enter pentru a reveni la meniu")
                
    if op == AFISARE_ORAS_BD_POPULATIE_MAXIMA:
        if len(arr) == 0:
            print ("Load the file first. What to insert ?")
        else:
            
           
            myCursor = mydb.cursor()
               
            sql = "SELECT `x`, `y`, `nume`, `judet`, `judetauto`, `populatie2002`, `regiune` FROM agendatelefonica.orase WHERE populatie2002 = (SELECT MAX(populatie2002) from agendatelefonica.orase)"
            myCursor.execute(sql)
            myRecords = myCursor.fetchone() 
            myCursor.close()
                
            print(myRecords)
        input("Apasati enter pentru a reveni la meniu")
           
    if op == STERGERE_ORAS_BD:
        if len(arr) == 0:
            print ("Load the file first. What to insert ?")
        else:
            orasulDeSters = input("ce oras doriti sa stergeti?: ")

            myCursor = mydb.cursor()
               
            sql = "DELETE  FROM agendatelefonica.orase WHERE nume = '" + orasulDeSters + "'"
            myCursor.execute(sql)
            myRecords = myCursor.fetchone() 
            myCursor.close()
                
            print("orasul", orasulDeSters, "a fost sters")
        input("Apasati enter pentru a reveni la meniu")
        
    if op == AFISARE_INFO_FISIER:
        f = open("orase.csv",'r')
        f.readline()
        
        for line in f:
            print(line)
                   
        f.close()
        input("Apasati enter pentru a reveni la meniu")
        
        
                   
        
        
        
        











mydb.close()             