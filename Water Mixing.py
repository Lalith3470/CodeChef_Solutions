for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(a<=b):
        if(b-a<=c):
            print("yes")
        else:
            print("no")
    else:
        if(a-b<=d):
            print("yes")
        else:
            print("no")
