for _ in range(int(input())):
    l=list(map(int, input().split()))
    l.sort()
    if l[0]+l[1]<l[2]:
        print("YES")
    else:
        print("NO")
