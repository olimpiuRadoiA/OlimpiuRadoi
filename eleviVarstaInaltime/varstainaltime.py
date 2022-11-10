
def citireFisier(numeFisier, arr):
    f = open(numeFisier,'r')   
    for line in f:
            
        arr.append(int(line))
    f.close()            
    return arr

def afisareFisier(arr):
    n = len(arr)    
    
    for i in range (0,n):
        print ( arr[i], end = " ") 
    
    
def sortare(arr):
    n = len(arr)
    for i in range (0,n-1):
        for j in range (i+1,n):
            if arr[i] > arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
            
    for i in range (0, n):
        print( arr[i], end= " ")
#main
varsta = []

citireFisier("varsta.txt", varsta)
print ("Varstele elevilor sunt: ")
afisareFisier(varsta)  
print( )
print ("sortati crescator")
sortare (varsta)                   


print()

inaltime = []
      
citireFisier("inaltimea.txt",inaltime)
print ("Inaltimile elevilor sunt: ")
afisareFisier(inaltime) 
print ( )
print ("sortati crescator")
sortare (inaltime)
                    



    
