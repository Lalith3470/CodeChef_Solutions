for _ in range(int(input())):
    x,y,s,p = map(int, input().split(' '))
    
    if x == 1 or y == 1 or s==1 or p == 1:
        print("OUT")
    else:
        print('IN')
        
