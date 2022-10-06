arr = [0] * 10

m = 10
n = 10

for y in range (0,m):
    for i in range (0,n):
        print(y+1, '*', (i+1), '=', (y+1)*(i+1), end = "   ",)
    print()
    print()