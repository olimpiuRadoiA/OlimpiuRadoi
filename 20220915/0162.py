arr = [0] * 100

n = int(input())

for i in range (0,n):
    arr[i] = int(input())
    

poz = n
for i in range (n, poz, -1):
        
    arr[i] = arr[i-1]

    
arr[poz] = arr[0]
n = n+1
    
i=0
while i<n:
    
    poz = i
    for j in range (poz,n):
        arr[j] = arr[j+1]
    n = n-1
    i = i+1
    

    
for i in range(0,n):
    print(arr[i], end=" ")