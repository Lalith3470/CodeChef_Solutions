t = int(input())

for i in range(t):
    a = int(input())
    
    if a > 65:
        print("Overload")
    elif a < 35:
        print("Underload")
    else:
        print("Normal")
