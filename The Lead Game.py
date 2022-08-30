n = int(input())
max=0
p1=0
p2=0

for i in range(n):
    a, b = map(int, input().split())
    p1 += a
    p2 += b
    diff=p1-p2
    
    if diff>0 and diff>max:
        max=diff
        leader=1

    elif diff<0 and abs(diff)>max:
        max=abs(diff)
        leader=2
print(leader,max)
