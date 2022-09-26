for _ in range(int(input())):
    a,b,c,d= map(int, input().split(' '))
    
    if (a==b and c==d) or (a==c and b==d) or (a==d and c==b):
        print("YES")
    else:
        print("NO")
