for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a<b:
        a=a+c
    else:
        b=b+c
    if a<b:
        a=a+d
    else:
        b=b+d
    if a>=b:
        print('N')
    else:
        print('S')
