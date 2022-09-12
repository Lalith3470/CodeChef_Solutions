for i in range(int(input())):
    x,y,x1,y1,D = map(int, input().split(' '))
    
    a = x//x1
    b = y//y1
    
    if min(a,b) >= D:
        print("YES")
    else:
        print("NO")
    
