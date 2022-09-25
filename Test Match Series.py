for _ in range(int(input())):
    a=list(map(int, input().split(' ')))
    count1=0
    count2=0
    for i in a:
        if i==1:
            count1+=1
        elif i == 2:
            count2+=1
    if count1==count2:
        print("DRAW")
    elif count1>count2:
        print("INDIA")
    else:
        print("ENGLAND")
