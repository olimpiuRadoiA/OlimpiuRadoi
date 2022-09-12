n = int(input())

arr = [0] * 100

for i in range (0,n,1):
    arr[i] = float(input())
    
inceputInterval = arr[0]
sfarsitInterval = arr[n-1]

if inceputInterval > sfarsitInterval:
    aux = inceputInterval
    inceputInterval = sfarsitInterval
    sfarsitInterval = aux

cate = 0
for i in range (0, n, 1):
    if arr[i] < inceputInterval or arr[i] > sfarsitInterval:
        cate = cate + 1

print(cate)



