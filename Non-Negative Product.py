# cook your dish here
for _ in range(int(input())):
    n = int(input())
    sum = 1
    a=list(map(int, input().split(' ')))
    for i in range(n):
        sum*=a[i]
    if sum>=0:
        print("0")
    else:
        print("1")
