for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split(' '))
    sum1 = x1+y1
    sum2 = x2+y2
    if sum1 > sum2:
        print(sum2)
    else:
        print(sum1)
