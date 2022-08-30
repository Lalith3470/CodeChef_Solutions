t = int(input())

for i in range(t):
    n = int(input())
    
    s = input()
    b = s.split()
    
    scount = 0
    tcount = 0
    for j in range(n):
        if b[j] == "START38":
            scount += 1
        else:
            tcount += 1
    print(scount, tcount)   
