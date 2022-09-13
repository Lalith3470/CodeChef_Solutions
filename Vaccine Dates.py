for _ in range(int(input())):
    D,L,R = map(int, input().split())
    if D in range(L,R+1):
        print("Take second dose now")
    else:
        if D<L:
            print("Too Early")
        else:
            print("Too Late")
