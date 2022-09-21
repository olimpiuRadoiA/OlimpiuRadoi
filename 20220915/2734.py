arr = [0] * 100

n = int(input())

for i in range (0,n):
    arr[i] = int(input())
    
i=0 
 

while i < n:
    
    if arr[i] == arr[n-i] :
        
        poz = i
        
        for j in range (poz,n):
            arr[j] = arr[j+1]
        n = n-1
    i = i+1
    
for i in range (0,n):
    print(arr[i], end =" ")
            
    