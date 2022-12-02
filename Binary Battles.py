for _ in range(int(input())):
    a,b,s=map(int, input().split())
    i=1
    c=0
    while i<a:
        if 2**i==a:
            c=i
            break
        else:
            i+=1
    print(b*c + s*(c-1))
