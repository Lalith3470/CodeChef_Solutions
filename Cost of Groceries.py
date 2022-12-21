for _ in range(int(input())):
    n,val=map(int, input().split())
    lst1=list(map(int, input().split()))
    lst2=list(map(int, input().split()))
    sm=0
    for i in range(n):
        if lst1[i]>=val:
            sm+=lst2[i]
    print(sm)
