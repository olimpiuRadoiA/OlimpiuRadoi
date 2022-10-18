

n = int(input())
m = int(input())

for i in range (n,m+1):
    for j in range (1,10):
        print(i,"*",j,"=",i*(j), end="   " )
    print()
