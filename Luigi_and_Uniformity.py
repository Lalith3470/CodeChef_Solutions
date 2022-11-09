# cook your dish here
for j in range(int(input())):
    a=int(input())
    d=list(map(int,input().split()))
    X=min(d)
    ans=0
    flag=0
    for l in range(a):
        if(d[l]!=X):
            if(d[l]%X==0):
                ans+=1
            else:
                flag=1
                break
    if(flag):
        print(a)
    else:
        print(ans) 
