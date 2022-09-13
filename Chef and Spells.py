for _ in range(int(input())):
    a,b,c = map(int, input().split(' '))
    
    sum = max((a+b),(a+c),(b+c))
    print(sum)
