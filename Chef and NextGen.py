for _ in range(int(input())):
    l=list(map(int, input().split()))
    if l[0]*l[1]>l[2]*l[3]:
        print("No")
    else:
        print("Yes")
