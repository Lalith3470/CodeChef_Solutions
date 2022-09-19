for _ in range(int(input())):
    low, high = map(int, input().split(' '))
    
    count=0
    for i in range(low,high+1):
        a = str(i)
        b = len(a)
        if int(a[b-1]) in (2,3,9):
            count+=1
            
            
    print(count)
