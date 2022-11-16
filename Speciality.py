for _ in range(int(input())):
    a,b,c=map(int, input().split())
    d=max(a,b,c)
    if d==a:
        print("Setter")
    elif d==c:
        print("Editorialist")
    else:
        print("Tester")
