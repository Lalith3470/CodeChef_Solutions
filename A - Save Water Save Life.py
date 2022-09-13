for _ in range(int(input())):
    H,x,y,C = map(int, input().split(' '))
    
    uasge = x+int((y/2))
    
    if H*uasge <= C:
        print("YES")
    else:
        print("NO")
