for _ in range(int(input())):
    X,Y = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    mini=0
    for i in range(X):
        if A[i] <= int(Y/2):
            mini+=abs(A[i]-Y)
        else:
            mini += abs(A[i]-1)
            
    print(mini)
