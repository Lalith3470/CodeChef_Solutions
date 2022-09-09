for i in range(int(input())):
    X,Y,P,Q = map(int, input().split(' '))
    chef = X + P*10
    chefina = Y + Q*10
    
    if chef == chefina:
        print("Draw")
    elif chefina > chef:
        print("Chef")
    else:
        print("Chefina")
