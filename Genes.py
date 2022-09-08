(a, b) = map(str, input().split(' '))
if a == 'R' or b == 'R':
    print("R")
elif a == b:
    print(a)
else:
    print("B")
