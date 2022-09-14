for _ in range(int(input())):
    N,k = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    sum = 0
    a=''
    for i in range(N):
        sum += A[i]
        if sum<=k:
            a+='1'
        else:
            a+='0'
            sum -=A[i]
    print(a)
