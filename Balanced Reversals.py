for _ in range(int(input())):
    n = int(input())
    a = input()
    l=''
    m=''
    for i in range(n):
        if a[i]=='1':
            l+='1'
        else:
            m+='0'
    print(m+l)
