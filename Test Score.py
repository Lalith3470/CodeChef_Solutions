for _ in range(int(input())):
    n,x,y=map(int, input().split())
    
    c=0
    for i in range(1,n+1):
        if x*i==y:
            c+=1
    if c==1 or y==0:
        print("YES")
    else:
        print("NO")
            
