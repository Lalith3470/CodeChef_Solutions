for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    
    total_candies = c*b
    
    if a%total_candies==0:
        print(a//total_candies)
    else:
    
        print((a//total_candies)+1)
