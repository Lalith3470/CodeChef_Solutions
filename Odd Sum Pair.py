for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (b+a)%2!=0 or (c+a)%2!=0:
        print("YES")
    else:
        print("NO")
