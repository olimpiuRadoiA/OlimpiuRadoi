#Print all prime numbers in the user-specified range.
#A number is prime if it is divisible only by itself and by one.
#For instance, 3 is a prime number, but 4 is not. 


arr = [0] * 100
n = int(input())
for i in range (0,n):
    arr[i] = int(input())


for i in range (0,n):
    prim = True
    d = 2
    while d<=int(arr[i]/2) and prim:
        if arr[i] % d == 0:
            prim = False
        d = d+1
        
    if prim == True:
        print( arr[i],", este prim; ", end=" ")
    
    





    
    