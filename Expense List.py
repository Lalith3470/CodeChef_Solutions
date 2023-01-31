for _ in range(int(input())):
    a,b=map(int, input().split())
    ans=2**b
    while a>0:
        ans=int(ans/2)
        a-=1
    print(ans)
