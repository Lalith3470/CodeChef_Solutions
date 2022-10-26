for _ in range(int(input())):
    n,q=map(int,input().split())
    l=list(map(int,input().split()))
    su=0
    for i in l:
        su+=i
    for i in range(q):
        a,b=map(int,input().split())
        if a-b==0:
            su+=1
        else:
            s=b-a+1
            if s%2!=0:
                c=int(s//2)
                d=s-c
                su+=c*-1
                su+=d*1
            
    print(su)
