for _ in range(int(input())):
    lst=list(map(int, input().split()))
    c=1
    if lst[0]==lst[2]:
        c+=1
    elif lst[1]==lst[3]:
        c+=1
    print(c)
