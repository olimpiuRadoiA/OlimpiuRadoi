arr = [0] * 10

n = int(input())
m = int(input())

for i in range (n,m+1):
    for j in range (0,10):
        print(i,"*",j+1,"=",i*(j+1), end="   " )
    print()