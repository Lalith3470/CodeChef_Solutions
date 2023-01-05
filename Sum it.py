for _ in range(int(input())):
    lst=list(map(int, input().split()))
    if lst[0]+lst[1]==lst[2]:
        print("YES")
    else:
        print("NO")
