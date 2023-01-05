import math
for _ in range(int(input())):
    a,b,c=map(int, input().split())
    i=2
    while i<100:
        if a%i!=0 and b%i!=0 and c%i!=0:
            print(i)
            break
        i+=1
