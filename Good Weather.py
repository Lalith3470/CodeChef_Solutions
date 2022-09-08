for i in range(int(input())):
    days = input()
    good_days = 0
    Bad_days = 0
    
    a = days.split()
    for i in range(len(a)):
        if a[i] == "1":
            good_days += 1
        else:
            Bad_days += 1
    
    if good_days >= Bad_days:
        print("YES")
    else:
        print("NO")
