

from math import sqrt


arr = [0] * 100

n = int(input())

for i in range (0,n):
    arr[i] = int(input())
    
    
i = 0
while i<n:
    if int(arr[i] / sqrt(arr[i])) == arr[i]:
        
        poz = i-1
        for j in range (n, poz, -1):
            arr[j] = arr[j+1]
        
        arr[poz] = sqrt(arr[i])
        n = n+1
        i = i+1
    i = i+1
    
for i in range (0,n):
    print(arr[i], end=" ")