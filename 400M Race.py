for _ in range(int(input())):
    lst=list(map(int, input().split()))
    lst[0]=400/lst[0]
    lst[1]=400/lst[1]
    lst[2]=400/lst[2]
    
    if max(lst)==lst[0]:
        print("ALICE")
    elif max(lst)==lst[1]:
        print("BOB")
    else:
        print("CHARLIE")
