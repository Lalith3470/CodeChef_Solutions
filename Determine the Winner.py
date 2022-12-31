for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if max(a,b)==max(c,d):
        print("TIE")
    elif max(a,b)>max(c,d):
        print("Q")
    else:
        print("P")
