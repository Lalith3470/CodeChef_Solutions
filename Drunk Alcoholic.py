def ans(n):
    odd_count = 0
    even_count = 0
    for i in range(1,n+1):
        if i%2 == 0:
            even_count+=1
        else:
            odd_count+=1
    
    total = odd_count*3 - even_count
    return total
    

for i in range(int(input())):
    n = int(input())
    
    print(ans(n))
