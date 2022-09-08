n = int(input())

arr = [0] * 100

for i in range(0,n,1):
    arr[i] = int(input())
sum = 0   
for i in range (0,n,1):
    sum = sum + arr[i]

print(sum)
for i in range (0,n,1):
    
    
        arr[i] = sum - arr[i]


for i in range (0,n,1):
    print(arr[i], end= " ")