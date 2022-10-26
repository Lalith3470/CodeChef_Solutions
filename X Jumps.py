for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%b==0:
        print(int(a/b))
    elif a<b:
        print(a)
    else:
        s=int(a/b)
        print(s+(a-s*b))
