for i in range(int(input())):
    (w, x, y, z) = map(int, input().split(' '))
    if x==w or y==w or z==w:
        print("YES")
    elif (x+y) == w or (x+z) == w or (y+z)==w or (x+y+z) ==w:
        print("YES")
    else:
        print("NO")
