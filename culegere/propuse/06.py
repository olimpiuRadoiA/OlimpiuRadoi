#Se dă un număr natural format din exact 4 cifre, prima cifră mai mare strict
#decât 1. Se cere să se afişeze numărul obţinut prin micşorarea cu 1 a fiecărei
#cifre.
#Exemplu: pentru numărul 3618 se va afişa 2507.

nr = int(input())

cate = 0
cnr = nr
while cnr > 0:
    cifra = cnr % 10
    cate = cate +1
    
    cnr = int(cnr/10)

print(cate)

if cate == 4:
    a = 1111

noulNr = nr - a

print(noulNr)