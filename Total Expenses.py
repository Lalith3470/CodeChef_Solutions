for i in range(int(input())):
    quantity, price = map(int, input().split())
    
    if quantity > 1000:
        sum = quantity / 10
        ans = quantity - sum
        print("{:.6f}".format(ans*price))
    else:
        print("{:.6f}".format(quantity*price))
