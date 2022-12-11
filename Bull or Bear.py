# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<b:
        print("LOSS")
    elif a>b:
        print("PROFIT")
    else:
        print("NEUTRAL")
