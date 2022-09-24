for _ in range(int(input())):
    a,b,c,d=map(int, input().split(' '))
    stock_perct = a*(d/100)

    total=a+stock_perct
    
    if total<=c and total>=b:
        print("Yes")
    else:
        print("No")
