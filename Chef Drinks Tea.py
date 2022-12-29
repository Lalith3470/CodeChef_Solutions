import math
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    sm= math.ceil(lst[0]/lst[1])
    print(sm*lst[2])
