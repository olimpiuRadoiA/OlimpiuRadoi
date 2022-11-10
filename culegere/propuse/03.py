#Se dă un număr natural cu exact trei cifre în variabila a. Se cere să se
#schimbe valoarea lui a (şi apoi să se afişeze) cu numărul obţinut prin
#înlocuirea cifrei zecilor cu cea a sutelor.

nr = int(input())

oglindit = 0
cnr = nr
while cnr > 0:
    cifra = cnr % 10
    oglindit = oglindit * 10 + cifra
    cnr = int(cnr/10)
    
print (oglindit)