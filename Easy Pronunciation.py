for _ in range(int(input())):
    T = int(input())
    S = list(map(str,input()))
    Subset = "schtschurowskia"
    count=0
    a=[]
    for char in range(len(S)):
        if S[char] in ('a','e','i','o','u'):
            count=0
        else:    
            count+=1
            if count>=4:
                break
        
    if count>=4:
        print("NO")
    else:
        print("YES")
                
