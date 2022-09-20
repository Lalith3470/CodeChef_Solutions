for _ in range(int(input())):
    a,b = map(int, input().split(' '))
    if a == b:
        print("ANY")
    elif a < b:
        print("REPAIR")
    else:
        print("NEW PHONE")
