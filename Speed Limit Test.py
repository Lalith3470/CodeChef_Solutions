for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    bob=c/d
    alice=a/b
    if bob > alice:
        print("Bob")
    elif bob<alice:
        print("Alice")
    else:
        print("Equal")
