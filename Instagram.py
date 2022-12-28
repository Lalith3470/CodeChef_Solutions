for _ in range(int(input())):
    lst = list(map(int,input().split()))
    if lst[1]*10 < lst[0]:
        print("Yes")
    else: print("No")
