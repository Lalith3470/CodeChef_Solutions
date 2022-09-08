def Ans(n):
    if n <= 18:
        return "1"
    elif n <= 24:
        return "2"
    elif n <=29:
        return "3"
    else:
        return "4"
        
        
for i in range(int(input())):
    (M, H) = map(int, input().split(' '))
    BMI = M/(H**2)
    
    print(Ans(BMI))
