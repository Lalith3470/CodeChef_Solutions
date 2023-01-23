a,b,c=map(int,input().split())
n=list(map(int, input().split()))
cnt=0
for i in n:
    if c+i==b:
        cnt+=1
if cnt>=1:
    print("YES")
else:
    print("NO")
