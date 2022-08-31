for _ in range(int(input())):
    int(input())
    ls = list(map(int,input().split()))
    max_count = 0
    for i in ls:
        ct = ls.count(i)
        if ct > max_count:
            max_count = ct
    swaps = len(ls)-max_count
    print(swaps)
