t = int(input())

for i in range(t):
    (m, n, k) = map(int, input().split(' '))
    
    sum = n*k
    if sum >= m:
        print("No")
    else:
        print("Yes")
