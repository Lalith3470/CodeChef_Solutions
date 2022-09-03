T = int(input())

for i in range(T):
    X, Y = map(int,input().split(' '))
    if Y%2 != 0 and X%2 != 0 or Y%2 == 0 and X%2 == 0:
        print("Janmansh")
    elif X%2 != 0 and Y%2 == 0:
        print("Jay")
    else:
        print("Jay")
