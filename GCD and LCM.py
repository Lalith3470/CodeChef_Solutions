for _ in range(int(input())):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        ans = (x*y)//gcd(x,y)
        return ans
    a,b=map(int, input().split())
    print(gcd(a,b),lcm(a,b))
