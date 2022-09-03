T = int(input())

for i in range(T):
    (n, x, p) = map(int,input().split(' '))
    
    if (p*2)+n >= x:
        print("yes")
    else:
        print("no")
