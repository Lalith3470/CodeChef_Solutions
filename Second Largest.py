T = int(input())

for i in range(T):
    (A, B, C) = map(int,input().split(' '))
    arr=[A,B,C]
    arr.sort()
    print(arr[-2])
    
