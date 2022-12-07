for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if a*c<b:
        print("YES")
    else:
        print("NO")
