for _ in range(int(input())):
    x,y,z=map(float,input().split())
    if x>50 and y<0.7 and z>5600 :
        print("10")
    elif x>50 and y<0.7 :
        print("9")
    elif y<0.7 and z>5600 :
        print("8")
    elif x>50 and z>5600 :
        print("7")
    elif x>50 or y<0.7 or z>5600 :
        print("6")
    else :
        print("5")
