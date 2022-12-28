for _ in range(int(input())):
    n=int(input())
    lst1=list(map(int, input().split()))
    lst2=list(map(int, input().split()))
    cnt=0
    lst=[]
    for i in range(n):
        if lst1[i]!=0 and lst2[i]!=0:
            cnt+=1
        else:
            lst.append(cnt)
            cnt=0
    lst.append(cnt)
    print(max(lst))
