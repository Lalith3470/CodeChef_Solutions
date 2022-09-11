for i in range(int(input())):
    (a, b, c) = map(int, input().split(' '))
    
    if (a+b)/2 < 35 or (c+b)/2 < 35 or (a+c)/2 < 35:
        print("Fail")
    else:
        print("Pass")
