for _ in range(int(input())):
    n,val=map(int, input().split())
    lst=list(map(int, input().split()))
    cnt=0
    for i in lst:
        if i>val:
            cnt+=1
    print(cnt)
