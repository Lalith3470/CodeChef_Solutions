for i in range(int(input())):
    N,X,Y = map(int, input().split(' '))
    capacity = (N+1)*Y
    
    if capacity >= X:
        print("YES")
    else:
        print("NO")
