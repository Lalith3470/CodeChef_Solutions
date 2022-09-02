t = int(input())

for i in range(t):
    (a, b, c) = map(int,input().split(' '))
    
    if a < b and a < c:
        print("Draw")
    else:
        if b > c:
            print("Alice")
        else:
            print("Bob")
