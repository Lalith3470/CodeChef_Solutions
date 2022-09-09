for i in range(int(input())):
    (X1, X2, Y1, Y2, Z1, Z2) = map(int, input().split(' '))
    
    if X1 <= X2 and Y1 <= Y2 and Z1 >= Z2:
        print("YES")
    else:
        print("NO")
    
