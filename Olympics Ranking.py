for i in range(int(input())):
    G1,S1,B1,G2,S2,B2 = map(int,input().split(' '))
    
    team1 = G1+S1+B1
    team2 = G2+S2+B2
    
    if team1 > team2:
        print("1")
    else:
        print("2")
