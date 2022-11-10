#Se dă un număr natural format din exact 4 cifre. Se cere să se afişeze suma
#pătratelor cifrelor numărului. 

nr = int (input())

cnr  = nr
suma = 0
while cnr > 0:
    cifra  = cnr % 10
    suma = suma + cifra*cifra
    cnr = int (cnr/10)
    
print (suma)