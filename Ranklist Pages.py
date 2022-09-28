for _ in range(int(input())):
    a=int(input())
    b=a/25
    if a%25!=0:
        print(int(b+1))
    else:
        print(int(b))
