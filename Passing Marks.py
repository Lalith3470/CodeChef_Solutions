for _ in range(int(input())):
    lst=list(map(int, input().split()))
    if lst[0]<=lst[4] and lst[1]<=lst[5] and lst[2]<=lst[6]:
        sm=lst[4]+lst[5]+lst[6]
        if sm>=lst[3]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
