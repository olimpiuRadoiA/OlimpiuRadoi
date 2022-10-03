import os

OP_EXIT = '9'

op = 0
while op != OP_EXIT:
    os.system("cls")
    
    
    print("1. Citire Array de la tastatura")
    print("2. citire Array Dinamic din fisier")
    print("3. Rezervat")
    print("4. Sortare")
    print("5. Inserare Element")
    print("6. Stergere Element")
    print("7. Minimm")
    print("8. Maxim")
    print("9. EXIT")
    
    op = input("Introduceti cifra corespunzatoare optiunii dorite: ")
    
    
    if op == '1':
        arr = [0] * 100
        n = int(input("cate elemente are Array-ul: "))
        print("Introduceti elementele ARRAY-ului")
        for i in range (0,n):
            arr[i] = int(input())
            
        for i in range (0,n):
            print (arr[i], end=" ")
        print()    
        input("Apasati ENTER pentru a reveni la meniu")
        
    if op == '2':
        arr = []
        f = open("D://Python//20221003//array.txt",'r')
       
        for line in f:
            arr.append(int(line))
        n = len(arr)
        
        for i in range (0,len(arr)):
            print(arr[i], end=" ")
               
        f.close()
        print()    
        input("Apasati ENTER pentru a reveni la meniu")    
         
    if op =='3':
        print("Optiune rezervata pentru viitor")
        print()    
        input("Apasati ENTER pentru a reveni la meniu")
        
    if op =='4':
        
        print("ce doriti sa sortati?", "apasati 41 pentru a introduce un array sau 42 pentru un array dinamic din fisier: ")
       
        OP4_EXIT = '43'
        op4 = 0
        while op4 != OP4_EXIT:
            os.system("cls")
    
    
            print("411. Sortare Crescatoare Array de la tastatura")
            print("412. Sortare Descrescatoare Array de la tastatura")
            print("421. Sortare crescatoare Array Dinamic din fisier")
            print("422. Sortare crescatoare Array Dinamic din fisier")
            print("43. EXIT")
        
            op4 = input("Introduceti cifra corespunzatoare optiunii dorite: ")
            if op4 == '411':
                arr = [0] * 100
                n = int(input("cate elemente are Array-ul: "))
                print("Introduceti elementele ARRAY-ului")
                for i in range (0,n):
                    arr[i] = int(input())
                for i in range (0,n-1):
                    for j in range (i+1,n):
                        if arr[i] > arr[j]:
                            aux = arr[i]
                            arr[i] = arr[j]
                            arr[j] = aux
                    
                for i in range (0,n):
                    print(arr[i], end=" ")
                print() 
                
                input("Apasati ENTER pentru a reveni la meniu")
                
            if op4 == '412':
                arr = [0] * 100
                n = int(input("cate elemente are Array-ul: "))
                print("Introduceti elementele ARRAY-ului")
                for i in range (0,n):
                    arr[i] = int(input())
                for i in range (0,n-1):
                    for j in range (i+1,n):
                        if arr[i] < arr[j]:
                            aux = arr[i]
                            arr[i] = arr[j]
                            arr[j] = aux
                    
                for i in range (0,n):
                    print(arr[i], end=" ")
                print() 
                
                input("Apasati ENTER pentru a reveni la meniu")
                
            if op4 == '421':
                arr = []
                f = open("D://Python//20221003//array.txt",'r')
       
                for line in f:
                    arr.append(int(line))
                n = len(arr)
        
                
                
                for i in range (0,len(arr)-1):
                    for j in range (i+1,len(arr)):
                        if arr[i] > arr[j]:
                            aux = arr[i]
                            arr[i] = arr[j]
                            arr[j] = aux
                    
                for i in range (0,len(arr)):
                    print(arr[i], end=" ")
                print() 
                f.close()
                
                input("Apasati ENTER pentru a reveni la meniu")     
                
            if op4 == '422':
                arr = []
                f = open("D://Python//20221003//array.txt",'r')
       
                for line in f:
                    arr.append(int(line))
                n = len(arr)
        
                
                
                for i in range (0,len(arr)-1):
                    for j in range (i+1,len(arr)):
                        if arr[i] < arr[j]:
                            aux = arr[i]
                            arr[i] = arr[j]
                            arr[j] = aux
                    
                for i in range (0,len(arr)):
                    print(arr[i], end=" ")
                print() 
                f.close()
                
                input("Apasati ENTER pentru a reveni la meniu")
    
    if op =='5':
        OP5_EXIT = '53'
        op5 = 0
        while op5 != OP5_EXIT:
            os.system("cls")
    
    
            print("51. Inserare Element in Array introdus de la tastatura")
            print("52. Inserare Element in Array Dinamic din fisier")
            print("53. EXIT")
        
            op5 = input("Introduceti cifra corespunzatoare optiunii dorite: ")       
            if op5 == '51':
                arr = [0] * 100
                n = int(input("cate elemente are Array-ul: "))
                print("Introduceti elementele ARRAY-ului")
                for i in range (0,n):
                    arr[i] = int(input())
                    
                elem = int(input("care este nu pe care doriti sa il introduceti: "))
                poz = int(input("pe ce pozitie introduceti noul nr: "))
                for i in range (n,poz,-1):
                    arr[i] = arr[i-1]
                    
                arr[poz] = elem
                n = n + 1
                
                
                for i in range (0,n):
                    print(arr[i], end=" ")
                print() 
                
                input("Apasati ENTER pentru a reveni la meniu")
                
            if op5 == '52':
                arr = []
                f = open("D://Python//20221003//array.txt",'r')
       
                for line in f:
                    arr.append(int(line))
                n = len(arr)

                elem = int(input("care este nu pe care doriti sa il introduceti: "))
                poz = int(input("pe ce pozitie introduceti noul nr: "))
                #for i in range (len(arr),poz,-1):
                #    arr[i] = arr[i-1]
                    
                #arr[poz] = elem
                #n=n+1
                
                
                for i in range (0,len(arr)):
                    print(arr[i], end=" ")
                print() 
                f.close()
                input("Apasati ENTER pentru a reveni la meniu")
                
    if op =='6':
        arr = [0] * 100
        n = int(input("cate elemente are Array-ul: "))
        print("Introduceti elementele ARRAY-ului")
        for i in range (0,n):
            arr[i] = int(input())
            
         
        poz = int (input("care este pozitia elemntului  pe care il stergeti?: "))    
        print("ati sters nr :",arr[poz] )
        
        for i in range (poz,n):
            
            arr[i] = arr[i+1]
        n = n - 1
        
        for i in range (0,n):
            print("noul arry este: ",arr[i], end=" ")
        print() 
                
        input("Apasati ENTER pentru a reveni la meniu")
        
    if op =='7':
        arr = [0] * 100
        n = int(input("cate elemente are Array-ul: "))
        print("Introduceti elementele ARRAY-ului")
        for i in range (0,n):
            arr[i] = int(input())
            
        minim = +2100000000
        for i in range (0,n):
            if minim > arr[i]:
                minim = arr[i]
        print("elementul cel mai mic este: ",minim)
        input("Apasati ENTER pentru a reveni la meniu")
    
        
    if op =='8':
        arr = [0] * 100
        n = int(input("cate elemente are Array-ul: "))
        print("Introduceti elementele ARRAY-ului")
        for i in range (0,n):
            arr[i] = int(input())
            
        maxim = -2100000000
        for i in range (0,n):
            if maxim < arr[i]:
                maxim = arr[i]
        print("elementul cel mai mare este: ",maxim)
        input("Apasati ENTER pentru a reveni la meniu")  
        
        
        
        
        
                
                    
          
        

    