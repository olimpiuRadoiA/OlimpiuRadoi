#Folosind formula 1+2+...+n = n(n+1)/2, afișați suma primelor 100, respectiv
#1000 de numere naturale.

n = int(input())

suma = 0
i = 0

while i <= n:
    suma = suma + i
    
    i = i+1
print ("altgoritmic")    
print (suma)

print ( )
print ("matematic")
rezolvareMatematica = n*(n+1) / 2
print(rezolvareMatematica)