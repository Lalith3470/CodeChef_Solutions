t = int(input())

for i in range(t):
    (x, m, d) = map(int, input().split(' '))
    minimum = min((x*m),(x+d))
    print(minimum)
