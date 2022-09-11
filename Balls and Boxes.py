for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    
    b = (b*(b+1))/2
    if a>=b:
        print("YES")
    else:
        print("NO")
