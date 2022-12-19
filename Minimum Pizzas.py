for _ in range(int(input())):
    a,b=map(int, input().split())
    c=(a*b)
    if c%4==0:
        print(int(c/4))
    else:
        print(int(c/4)+1)
