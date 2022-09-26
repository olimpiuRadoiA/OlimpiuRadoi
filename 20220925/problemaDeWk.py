arr = [0] * 100
nr = int (input())

cnr = nr
cate = 0
i = 0
while cnr > 0:
    cifra = cnr % 10
    cate = cate + 1
    arr[i] = cifra
    i = i + 1
    cnr = int(cnr/10)
        
print(cate)    
    
for i in range(0,cate-1):
    for j in range(i+1,cate):
        if arr[i] > arr[j] :  
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux   

nr1 = 0
for i in range(0,cate):
    nr1 =nr1 + (arr[i] * 10**(cate-i-1))   
print(nr1)
    
for i in range(0,cate-1):
    for j in range(i+1,cate):
        if arr[i] < arr[j] :  
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux   

nr2 = 0
for i in range(0,cate):
    nr2 = nr2 + (arr[i] * 10**(cate-i-1))
print(nr2)

if nr2 >= nr1:
    raspuns = nr2-nr1
else:
    raspuns = nr1-nr2    
print(raspuns)
            
    
     




    
  
    

