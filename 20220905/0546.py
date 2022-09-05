n = int(input())

arr = [0]*100

for i in range (0,n,1):
    arr[i] = int(input())
rezultat = 0    
for i in range (0,n,1):
    if arr[i] % arr[n-1] == 0:
        
        print(arr[i], end=" ")