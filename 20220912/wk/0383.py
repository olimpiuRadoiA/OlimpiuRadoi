

k = int(input("nr nat nenul: "))
   
    

arr = [0] * 100

n = int(input())

for i in range (0, n, 1):
    arr[i] = int(input())
    
    
aux = 1
for i in range (0, n, 1):
    aux = int(arr[i]/k)
    if (aux * k) - arr[i] < 0:
        pos1 = (-1) * ((aux * k) - arr[i])
    pos2 = ((aux+1)*k) - arr[i]
    if pos1 < pos2:
        aux = k * (int(arr[i]/k))
    else:
        aux = k * (int(arr[i]/k) + 1)

    arr[i] = aux
    
    

for i in range (0, n, 1):
    i = n - 1 - i
    print(arr[i], end=" ")
      
    

          
    

   