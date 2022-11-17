for _ in range(int(input())):
    a,b=map(int, input().split())
    if 100*a >= 10*b:
        print("Cloth")
    else:
        print("Disposable")
