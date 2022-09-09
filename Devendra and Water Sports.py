for i in range(int(input())):
    Z,Y,A,B,C = map(int, input().split(' '))
    total_money = Z-Y
    spend_money = A+B+C
    
    if total_money >= spend_money:
        print("YES")
    else:
        print("NO")
