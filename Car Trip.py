def cost(a):
    if a <= 300:
        return "3000"
    else:
        return a*10


for i in range(int(input())):
    a = int(input())
    
    print(cost(a))
