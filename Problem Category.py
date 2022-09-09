def ans(n):
    if n < 100:
        return "Easy"
    elif n < 200:
        return "Medium"
    else:
        return "Hard"


for i in range(int(input())):
    rating = int(input())
    
    print(ans(rating))
