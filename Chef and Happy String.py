for _ in range(int(input())):
    temp="aeiou"
    gvn=input()
    c=0
    lst=[0]
    for i in gvn:
        if i in temp:
            c+=1
        else:
            lst.append(c)
            c=0
    lst.append(c)
    
    if max(lst)>2:
        print("Happy")
    else:
        print("Sad")
