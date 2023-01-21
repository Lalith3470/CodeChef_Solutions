for _ in range(int(input())):
    l1=list(map(int, input().split()))
    l2=list(map(int, input().split()))
    if l1.count(1)==l2.count(1):
        print("Pass")
    else:
        print("Fail")
