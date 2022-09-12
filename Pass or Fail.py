T = int(input())
for i in range(T):
    (n, x, p) = map(int,input().split(' '))
    
    sum = (n-x)*1 
    if (x*3)-sum >= p:
        print("Pass")
    else:
        print("Fail")
