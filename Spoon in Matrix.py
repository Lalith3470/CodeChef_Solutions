# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    lst=[]
    for i in range(a):
        lst.append(input().lower())
    lst2=[]
    val=False
    for i in lst:
        if 'spoon' in i:
            val=True
            break
    if not val:
        for i in zip(*lst):
            i=''.join(i)
            if 'spoon' in i:
                val=True
                break
    if val:print("There is a spoon!")
    else:print("There is indeed no spoon!")
    
