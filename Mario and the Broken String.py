for _ in range(int(input())):
    n=int(input())
    a=input()
    if a[:int(n/2)]==a[int(n/2):]:
        print("YES")
    else:
        print("NO")
