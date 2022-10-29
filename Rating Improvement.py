for _ in range(int(input())):
    x,y=map(int, input().split())
    if y>=x and y<=x+200:
        print("YES")
    else:
        print("NO")
