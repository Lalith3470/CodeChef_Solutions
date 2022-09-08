for i in range(int(input())):
    (X, Y, Z) = map(int, input().split(' '))
    
    if X+Y < Z:
        print("PLANEBUS")
    elif X+Y == Z:
        print("EQUAL")
    else:
        print("TRAIN")
