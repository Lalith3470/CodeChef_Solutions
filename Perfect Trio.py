# cook your dish here
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    lst.sort()
    if lst[-1]==sum(lst[:2]):
        print("YES")
    else:print("NO")
