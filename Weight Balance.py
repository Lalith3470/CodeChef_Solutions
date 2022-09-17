for _ in range(int(input())):
    w1,w2,x1,x2,M = map(int, input().split())
    weight = w2-w1
    wt_mt_1=x1*M
    wt_mt_2=x2*M
    if weight >= wt_mt_1 and weight<=wt_mt_2:
        print("1")
    else:
        print('0')
