for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    sum = b+(c*2)
    if sum <= a:
        print("YES")
    else:
        print("NO")
