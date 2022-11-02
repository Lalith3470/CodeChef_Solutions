for _ in range(int(input())):
    a,b=map(int, input().split())
    m=a*2
    n=b*5
    if m==n:
        print("Either")
    elif m>n:
        print("Chocolate")
    else:
        print("Candy")
