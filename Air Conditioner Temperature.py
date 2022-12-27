for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if a<=b and b>=c:
        print("YES")
    else:
        print("NO")
