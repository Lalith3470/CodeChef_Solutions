# cook your dish here
for _ in range(int(input())):
    n = int(input())
    count=0
    i_count=0
    s = input()
    for i in range(n):
        if s[i] == 'I':
            i_count+=1
        elif s[i]=='N':
            count+=1
        else:
            count=0
            
    if i_count>0:
        print("INDIAN")
    elif count==len(s):
        print("NOT SURE")
    else:
        print("NOT INDIAN")
