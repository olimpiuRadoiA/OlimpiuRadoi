h1 = int(input())
m1 = int(input())
x  = int(input())
h2 = 0
m2 = 0

if x < 60:           #brut si daca valoarea lui x>100 e cu eroare
    m2 = m1 + x
    if m2 >= 60:
        m2 = m2 - 60
        h2 = h1 + 1
    print (h2,":",m2)

if x > 60:              #brut si daca valoarea lui x>100 e cu eroare
    m2 = m1 + x - 60
    h2 = h1 + int(x/60)
    print(h2,":",m2)
    
i = 0
n = 60
while i < n:
    m3 = m1 + n
    if m3 >= n:
        m3 = m1 + (x - (int(x/60)*60))
        h3 = h1 + int(x/60)
    
    i = i+1
print (h3,":",m3)    
 
    
    
  