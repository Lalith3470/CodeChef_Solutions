for _ in range(int(input())):
    lst=list(map(int, input().split()))
    ans=int(lst[2]/lst[0])+int(lst[3]/lst[1])
    print(ans)
