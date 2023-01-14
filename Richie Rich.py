for _ in range(int(input())):
    lst=list(map(int, input().split()))
    ans=(lst[1]-lst[0])/lst[2]
    print(int(ans))
