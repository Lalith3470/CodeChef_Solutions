for _ in range(int(input())):
    n,b = map(int, input().split(' '))
    g = 0
    sum = []
    for i in range(n):
        
        W,H,P = map(int, input().split(' '))
        
        if P<=b:
            g +=1
            sum.append(H*W)
            
    if g>=1:
        print(max(sum))
    else:
        print("no tablet")
    
