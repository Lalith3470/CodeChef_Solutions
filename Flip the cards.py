for _ in range(int(input())):
    a,b=map(int, input().split(' '))
    if a==b or b==0:
        print('0')
    elif a-b > int(a/2):
        print(b)
    else:
        print(a-b)
