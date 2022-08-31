def result(n):
    s = n[::-1]
    if s == n:
        return "wins"
    else:
        return "loses"

t = int(input())

for i in range(t):
    n = input()
    print(result(n))
