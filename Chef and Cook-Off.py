for _ in range(int(input())):
    l=list(map(int,input().split()))
    sm=sum(l)
    if sm==0:
        print("Beginner")
    elif sm==1:
        print("Junior Developer")
    elif sm==2:
        print("Middle Developer")
    elif sm==3:
        print("Senior Developer")
    elif sm==4:
        print("Hacker")
    else:
        print("Jeff Dean")
