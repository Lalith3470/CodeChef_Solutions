from collections import Counter
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int, input().split()))
    cnt=Counter(lst)
    c=0
    for j in cnt.values():
        if j%2!=0:
            c+=1
    if c>0:
        print("No")
    else:
        print("Yes")
