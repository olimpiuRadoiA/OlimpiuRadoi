from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import unittest
import mysql.connector



hostName = "localhost"
serverPort = 8080

class StringUtils:
    def indexOf(self, text, deCautat):    
        try:
            poz = text.index(deCautat)
        except:
            poz = -1
        return poz

class HttpGETParam:
    
    def __init__(self, pair):
        self.param = ""
        self.values = []
        su = StringUtils()
        poz = su.indexOf(pair, "=")
        if( poz >-1):
            self.param = pair[0:poz]
            value = pair[poz+1:]

            poz = su.indexOf(value, ",")
            while poz > -1:
                elem = value[0:poz]
                self.values.append(elem)
                value = value[poz+1:]

                poz = su.indexOf(value, ",")
            self.values.append(value)
        else:
            self.param = "notValid"
            self.values.append("notValid")    
        
        
class URLSplitter:
   
    def __init__(self, url):
        self.protocol = "" 
        self.content = ""
        self.domainName = ""
        self.domainType = ""
        self.port = ""
        self.application = ""
        self.folders = []
        self.resource = ""
        self.getParams = []

        su = StringUtils()
        
        poz = su.indexOf(url, "://")
        if(poz > -1):
            self.protocol = url[0:poz]
           
            url = url[poz+3:]
            
        
        poz = su.indexOf(url, "?")
        if poz == su.indexOf(url, "?") and (poz > -1):
            textOfGetParams = url[poz+1:]

            poz = su.indexOf(textOfGetParams, "&")
            while poz > -1 :
                oneGetParam = textOfGetParams[0:poz]
                getParam = HttpGETParam(oneGetParam)
                self.getParams.append(getParam)
                textOfGetParams = textOfGetParams[poz+1:]
                poz = su.indexOf(textOfGetParams, "&")
                
            
            oneGetParam = textOfGetParams
            getParam = HttpGETParam(oneGetParam)
            self.getParams.append(getParam)
           
        poz = su.indexOf(url,"/")
        if (poz>-1):
            domain = url[0::]
            
            poz = su.indexOf(domain,"/")
            if (poz>-1):
                domain2 = domain[0:poz]
            
                poz = su.indexOf(domain2,":")
                if poz == su.indexOf(domain2,":") and (poz >-1):
                    self.port = domain2[poz+1::]
                    print("port",self.port)
                domain2 = domain2[0:poz]
                
                poz = su.indexOf(domain2,".")
                    
                if poz == su.indexOf(domain2,".") and (poz>-1):              
                    self.content = domain2[0:poz]
                    
                    domain2 = domain2[poz+1::]
                    self.domainName = domain2[0:poz]
                    
                    domain2 = domain2[poz+1::]
                    self.domainType = domain2
                    print(self.domainType)
                        
            poz = su.indexOf(domain,'?')
            if poz == su.indexOf(domain,'?') and (poz > -1):
                url = domain[0:poz] 
              
            else:
                url = domain[0::] 
                               
                    
            poz = su.indexOf(url, "/")
            if poz == su.indexOf(url, "/") and poz > -1:
                allFolders = url[poz+1::]
                
                poz = su.indexOf(allFolders, ".") 
                if poz == su.indexOf(allFolders, ".") and (poz > -1):
                    self.resource = allFolders
                    
                poz = su.indexOf(allFolders, "/")
                                    
                if poz == su.indexOf(allFolders, "/") and (poz > -1):
                                
                    self.application = allFolders[0:poz] 
                    
                    allFolders = allFolders[poz+1:] 

                    poz = su.indexOf(allFolders, "/")
                            
                    while (poz > -1):
                        folder = allFolders[0:poz]  
                        allFolders = allFolders[poz+1:]
                                    
                        poz = su.indexOf(allFolders, "/") # actualizez pozitia /
                        self.folders.append(folder)
                                
                    self.resource = allFolders

class MyServer(BaseHTTPRequestHandler):
     
    def getFileName(self):
        urlDetails = URLSplitter(self.path)
        fileName = urlDetails.resource
        #fileName = "test.html"
        
        return fileName
    
    def getParams(self):
        urlDetails = URLSplitter(self.path)
        params = urlDetails.getParams
        print(params)
        
    def getFolder(self):
        urlDetails = URLSplitter(self.path)
        folder = urlDetails.application
        print(folder)
    
    def exists(self, fileName): # cum identific o erroare daca nu am dat de ea (de genul FileNotFoundError )...pt a folosi try si except?
     
        gotTheFile = True
        
        try:
                
            f = open('C:\\Users\\olyal\\Documents\\Python\\20230313\\' + fileName,'r')  # mai tre' studiat
            
            f.close()
        except FileNotFoundError:
            gotTheFile = False
        return gotTheFile
    
    def isFile(self, fileName):
        gotTheExtention = False
        fileName = self.getFileName()
        su = StringUtils()
        poz = su.indexOf(fileName,".")
        
        if poz > -1:
            gotTheExtention = True
        
        return gotTheExtention    
    
    def getExtension(self, fileName):
        fileName = self.getFileName()
        su = StringUtils()
        poz = su.indexOf(fileName,".")
        
        if poz > -1:
            extensie = fileName[poz::]
            
        return extensie    
    
    def writeFileInResponse(self, fileName):
        
        os.chdir("Documents")
        os.chdir("Python\\20230313\\")
        
        fileName = self.getFileName()
       
        f = open( fileName,'r')
        extensie = self.getExtension(fileName)
      
        if extensie == ".html":
            for line in f:
                self.wfile.write(bytes(line, "utf-8"))
        if extensie != ".html":     
            contentFile = f.read()
            self.wfile.write(bytes(contentFile, "utf-8"))
        
        
        f.close()
    

    
    
    def do_GET(self):
        
        fileName = self.getFileName()
        
        print("aha",fileName)
        if (self.isFile(fileName)):
            if (self.exists(fileName)):
                print("path",self.path)
                if self.path == '/favicon.ico':
                    self.send_response(404)
                    print("ERROR Accepted")
                        
                if self.path != '/favicon.ico':
                        
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.writeFileInResponse(self.getFileName())
            else:
                self.send_response(404)
                print(" I don't know what s this")
        
        action = self.getFolder()
        if action == "authentificate":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.writeFileInResponse(self.getFileName())
            print("aha01")
            user = ""
            password = ""
            params = self.getParams()
            for param in params:
                if param == "email":
                    user = params[0]
            
            for param in params:
                if param == "password":
                    password = params[0]       
               
            if user != "" and password != "":
                
                credential = Db(user,password)
                
                if credential:
                    print("utlizatorul exista")
                else:
                    print("utlizatorul NU exista")
        
webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:  #CTRL+C
    pass

class Db():
    def __init__(self,user,password):    
        mydb = mysql.connector.connect ( host="localhost", port="3306",user="valoriMihai", password="1234", database ="login" )

        myCursor = mydb.cursor()
        
        
        
        dateTabel="SELECT * FROM login.userpassword WHERE user=%s AND password = %s;"
        valori=(user,password)
        myCursor.execute(dateTabel, valori)          
        
        result = myCursor.fetchone()

        if result:
            print("Utilizatorul există în baza de date.")
        else:
            print("Utilizatorul nu există în baza de date.")
          
        mydb.commit()  
    
    

class TestHttpGETParam(unittest.TestCase):
    
    def testGoodPairParamOneValue(self):
        pair = "username=mihai"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "username", getParam.param)

    def testGoodPairParamMultipleValueFirst(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "EUR", getParam.values[0])

    def testGoodPairParamMultipleValueSecond(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "RON", getParam.values[1])

    def testGoodPairParamMultipleValueLast(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "USD", getParam.values[2])

    def testNoEquals(self):
        pair = "username"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "notValid", getParam.param)

class TestURLSplitter(TestHttpGETParam):
    
    def testGoodPairParamOneValue(self):
        pair = "username=mihai"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "username", getParam.param)

    def testGoodPairParamMultipleValueFirst(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "EUR", getParam.values[0])

    def testGoodPairParamMultipleValueSecond(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "RON", getParam.values[1])

    def testGoodPairParamMultipleValueLast(self):
        pair = "currencies=EUR,RON,USD"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "USD", getParam.values[2])

    def testNoEquals(self):
        pair = "username"
        getParam = HttpGETParam(pair)
        
        self.assertEqual( "notValid", getParam.param)

class TestURLSplitter(TestHttpGETParam):
    
    def testProtocolHttp(self):
        url = "http://www.google.com"
        urlDetails = URLSplitter(url)
        
        self.assertEqual( "http", urlDetails.protocol)
  
    def testProtocolHttps(self):
        url = "https://www.cnn.com"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("https", urlDetails.protocol)

    def testProtocolEmpty(self):
        url = "://www.cnn.com"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("", urlDetails.protocol)

    def testProtocolNoProtocol(self):
        url = "www.cnn.com"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("", urlDetails.protocol)


    def testOneGetParam(self):
        url = "http://www.cnn.com:8080/aplicatie/resource.html?username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual(1, len(urlDetails.getParams))

    def testProperValueOfOneGetParam(self):
        url = "http://www.cnn.com:8080/aplicatie/resource.html?username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("mihai", urlDetails.getParams[0].values[0])

    def testProperValueOfOneGetParamMultipleValues(self):
        url = "http://www.cnn.com:8080/aplicatie/resource.html?currency=EUR,RON,USD"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("EUR", urlDetails.getParams[0].values[0])

    def testProperValueOfTwoGetParamMultipleValuesFirst(self):
        url = "http://www.cnn.com:8080/aplicatie/resource.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("EUR", urlDetails.getParams[0].values[0])
        
    def testProperValueOfTwoGetParamMultipleValuesSecond(self):
        url = "http://www.cnn.com:8080/aplicatie/resource.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("mihai", urlDetails.getParams[1].values[0])
    
    def testProperValueOfAplicatie(self):
        url = "http://www.cnn.com:8080/salarii/folder1/folder2/resource.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("salarii", urlDetails.application)
    
    def testProperValueOfFolders(self):
        url = "http://www.cnn.com:8080/salarii/folder1/folder2/resource.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("folder1", urlDetails.folders[0])
    
    def testProperValueOfResource(self):
        url = "http://www.cnn.com:8080/salarii/folder1/folder2/dashboard.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("dashboard.html", urlDetails.resource)
    
    def testProprtValueResource(self):
        url = "/salarii/folder1/folder2/dashboard.html?currency=EUR,RON,USD&username=mihai"
        urlDetails = URLSplitter(url)
        self.assertEqual("dashboard.html", urlDetails.resource)
    
    def testProperValueOfResource01(self):
        url = "http://localhost:8080/test.html"
        urlDetails = URLSplitter(url)
        
        self.assertEqual("test.html", urlDetails.resource)

webServer.server_close()
print("Server stopped.")