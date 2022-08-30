t = int(input())

for i in range(t):
    s = input()
    t = input()
    
    a = ""
    for j in range(len(s)):
        if s[j] == t[j]:
            a += "G"
        else:
            a += "B"
    
    print(a)
