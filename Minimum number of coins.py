for _ in range(int(input())):
    n=int(input())
    ans=int(n/10)
    ans1=n-ans*10
    ans2=int(ans1/5)
    sol=n-ans2*5-ans*10
    if sol>0:
        print(-1)
    else:
        print(ans2+ans)
