#Se dă un număr natural x cu maxim 3 cifre. Se cere să se afişeze suma
#cuburilor cifrelor lui x.

x = int(input())

cX = x
suma = 0
while cX > 0:
    cifra = cX % 10
    suma = suma + (cifra * cifra * cifra)
   
    cX = int(cX/10)
    
print (suma)