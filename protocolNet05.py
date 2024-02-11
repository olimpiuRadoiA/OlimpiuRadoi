import requests
import mysql.connector
from datetime import datetime

def indexOf(line, deCautat):
    poz = -1
    try:
        poz = line.index(deCautat)
    except:
        poz = -1
    return poz

def findCharInText(text, char):
    poz = -1
    for i in  range(0, len(text)):
        if text[i] == char:
            poz = i
    return poz

def removLeadingWhitespace(string):
    return string.lstrip()

def bazaValoriAer(temperature,humidity,preasure):
    dateTabel="INSERT INTO tempumidpress.valuefromhome (temperature,humidity,preasure) VALUES (%s,%s,%s)"
    valori = (temperature,humidity,preasure)
              
    myCursor.execute(dateTabel,valori)
    mydb.commit()        
   
# forever = True

# while forever == True:
    
protocol = "http"
ip = "136.255.226.122"

port = 60001

uri = "html" # cu er printeza 500

url = protocol + "://" + ip + ":" + str(port) + "/" + uri

response  = requests.get( url )


if response.status_code == 404:
    print("Page Not Found")
    #forever = False
    
if response.status_code == 401:
    print("Authentification required")
    #forever = False
    
gotIt = True   
if response.status_code == 200:
    print(response.text) # OK
    gotIt = True
        
if gotIt == False:
    print(response.status_code) 
    #forever = False
text = response.text

faraimportanta1 = text[0:text.index('<td>')]
text            = text[text.index('<td>'):]
temp            = text[4:text.index('</td>')]
text            = text[text.index('</td>'):]
faraimportanta2 = text[text.index('</td>'):text.index('<td>')]
text            = text[text.index('<td>'):]
valTemp         = text[4:text.index('</td>')]
text            = text[text.index('</td>'):]
faraimportanta3 = text[text.index('</td>'):text.index('<td>')]
text            = text[text.index('<td>'):]
umid            = text[4:text.index('</td>')]
text            = text[text.index('</td>'):]
faraimportanta4 = text[text.index('</td>'):text.index('<td>')]
text            = text[text.index('<td>'):]
valUmid         = text[4:text.index('</td>')]
text            = text[text.index('</td>'):]
faraimportanta5 = text[text.index('</td>'):text.index('<td>')]
text            = text[text.index('<td>'):]
press           = text[4:text.index('</td>')]
text            = text[text.index('</td>'):]
faraimportanta6 = text[text.index('</td>'):text.index('<td>')]
text            = text[text.index('<td>'):]
valPress        = text[4:text.index('</td>')]
faraimportanta7 = text[text.index('</td>'):]




print(temp.strip())
print(valTemp.strip())
print(umid.strip())
print(valUmid.strip())
print(press.strip())
print(valPress.strip())

temperature     = temp.strip()
vTemperature    = valTemp.strip()
humidity        = umid.strip()
vHumidity       = valUmid.strip()
preasure        = press.strip()
vPeasure        = valPress.strip()

forever = True
nrDeIncarcariInDb = 1

while forever == True:
    nrDeIncarcariInDb == 1
    vTemperatureDeTrimis = vTemperature
    if vTemperatureDeTrimis == vTemperature:
        mydb = mysql.connector.connect ( host="localhost", port="3306", user="valoriMihai", password="1234", database ="tempumidpress" )

        myCursor = mydb.cursor()


        bazaValoriAer(vTemperature,vHumidity,vPeasure)    
        
        
        mydb.close()

        nrDeIncarcariInDb = 1
        
    else: 
        mydb = mysql.connector.connect ( host="localhost", port="3306", user="valoriMihai", password="1234", database ="tempumidpress" )

        myCursor = mydb.cursor()


        bazaValoriAer(vTemperature,vHumidity,vPeasure)    
        
        
        mydb.close()
        
    
   



     


