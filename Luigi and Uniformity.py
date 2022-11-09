for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    cnt=0
    c=min(l)
    for i in l:
        if i%c!=0:
            cnt+=1
            break
    if cnt==1:
        print(n)
    else:
        print(n-l.count(c))
        
