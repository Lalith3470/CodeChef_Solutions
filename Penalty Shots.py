for _ in range(int(input())):
    a = list(map(int, input().split()))
    
    team2 = 0
    team1 = 0
    for i in range(0,10,2):
        team1 += a[i]
    
    for i in range(1,10,2):
        team2 += a[i]
        
    if team1 > team2:
        print(1)
    elif team1 == team2:
        print(0)
    else:
        print(2)
