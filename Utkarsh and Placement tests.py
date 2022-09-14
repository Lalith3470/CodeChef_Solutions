for i in range(int(input())):
    A = input()
    B = A.split()
    x,y = map(str, input().split(' '))
    
    x_count = 0
    y_count = 0
    for i in range(3):
        if B[i] == x:
            x_count = i
        elif B[i] == y:
            y_count = i
    
    
    if x_count > y_count:
        print(B[y_count])
    else:
        print(B[x_count])
    
