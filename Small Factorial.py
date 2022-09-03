t = int(input())
for i in range(t):
    fac = 1
    N = int(input())
    for j in range(1,N+1):
        fac *= j

    print(fac)
