x = [0] * 100
n = int(input())

for i in range (0, n, 1):
    x[i] = int(input())
    
y = [0] * 100    
m = int(input())

for i in range (0, m, 1):
    y[i] = int(input())
    
minim = 2100000000    
for i in range (0, m, 1):
    if y[i] < minim:
        minim = y[i]
        
for i in range (0, n, 1):
    if x[i] < minim:
        print(x[i], end = " ")

