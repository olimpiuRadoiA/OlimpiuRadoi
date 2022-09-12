arr = [0] * 100

n = int(input())

for i in range (0,n,1):
    arr[i] = int(input())

cate = 0   
suma = 0
aux = 0
for i in range (0, n, 1):
    if arr[i] != 0:
        suma = suma + arr[i]
        cate = cate + 1
for i in range (0, n, 1):    
    if arr[i] == 0:
        arr[i] = aux
        aux = int(suma/cate)
        arr[i] = aux
    else:
        arr[i] = arr[i] 
        
   
for i in range (0, n, 1):
    print(arr[i], end = " ")    
   
       