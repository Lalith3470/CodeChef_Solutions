for _ in range(int(input())):
    p,w=map(int, input().split())
    if p*w <=500 and p<=8:print("YES")
    else:print("NO")
