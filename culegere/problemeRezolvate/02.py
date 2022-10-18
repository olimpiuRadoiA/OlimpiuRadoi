# Afișați suma dintre penultima și ultima cifră a anului curent folosind o expresie aritmetică.

n = int(input("Tastati anul curent: "))

sumaUltimelor2Cifre = 0
cn = n
while cn > 2:
    cifra = cn % 10
    sumaUltimelor2Cifre = sumaUltimelor2Cifre + cifra
    cn = int(cn/10)

print (sumaUltimelor2Cifre)
    