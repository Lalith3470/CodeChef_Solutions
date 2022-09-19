(p1, p2, p3, p4) = map(int,input().split(' '))

count = 0
for i in range(4):
    if p1 >= 10:
        count += 1
    
print(count)
