# cook your dish here
for _ in range(int(input())):
    a = int(input())
    if a<=100:
        print(a)
    elif a<=1000:
        print(a-25)
    elif a<=5000:
        print(a-100)
    else:
        print(a-500)
