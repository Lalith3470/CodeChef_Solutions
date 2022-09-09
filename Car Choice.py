for i in range(int(input())):
    X1,X2,Y1,Y2 = map(int,input().split(' '))
    car1 = Y1/X1
    car2 = Y2/X2
    
    if car2 == car1:
        print("0")
    elif car1 > car2:
        print("1")
    else:
        print("-1")
