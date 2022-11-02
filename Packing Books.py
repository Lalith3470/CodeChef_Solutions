for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if b%c == 0:
        print(a*(b//c))
    else:
        print(a*(b//c+1))
