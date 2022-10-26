for _ in range(int(input())):
    a,b=map(int,input().split())
    if b%a==0 or a==b:
        print("YES")
    elif b-2*a<0:
        print("NO")
    else:
        print("YES")
