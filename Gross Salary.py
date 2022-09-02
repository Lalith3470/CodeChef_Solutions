t = int(input())

for i in range(t):
    basic = int(input())
    
    if basic < 1500:
        hra = basic*0.1
        da = basic*0.90
        gross_salary = basic + hra + da
        
        print(gross_salary)
    
    else: 
        hra = 500
        da = basic * 0.98
        gross_salary = basic + hra + da
        
        print(gross_salary)
        
