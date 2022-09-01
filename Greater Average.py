for i in range(int(input())):
    a = input()
    b = a.split()
    avg = float((int(b[0])+int(b[1]))/2)
    if avg > int(b[2]):
        print("YES")
    else:
        print("NO")
