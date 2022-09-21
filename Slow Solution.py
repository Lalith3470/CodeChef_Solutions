for i in range(int(input())):
    maxT,maxN,sumN=map(int,input().split())
    sum=0
    while((sumN!=0) and maxT):
        if(maxN<=sumN):
            sum+=maxN**2
            sumN=sumN-maxN 
        else:
            sum+=sumN**2
            sumN=0
        maxT-=1
    print(sum)
