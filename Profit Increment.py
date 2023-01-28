for _ in range(int(input())):
    a,b=map(int, input().split())
    ans=a+(a/10) - (a-b)
    print(int(ans))
