arr = [0] * 100

n = int(input())

for i in range (0,n):
    arr[i] = int(input())
    
i = 0

while i < n-1:
    if (arr[i] % 2 == 0 and arr[i+1] % 2 == 0) or (arr[i] % 2 == 1 and arr[i+1] % 2 == 1):
        media = int((arr[i]+arr[i+1])/2)
        poz = i+1
        for j in range (n,poz,-1):
            arr[j] = arr[j-1]
        arr[poz] = media
        n = n+1
        i=i+1
    i = i+1
    
for i in range (0,n):
    print(arr[i], end=" ")    
    