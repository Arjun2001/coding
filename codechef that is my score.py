import math
test=int(input())
while(test):
    n=int(input())
    ans=list(map(int,input().split()))
    z=t=0
    for i in ans:
        if i==0:
            z+=1
        elif i==2:
            t+=1
    if z>=2:
        z=math.factorial(z)//(2*math.factorial(z-2))
    else:
        z=0
    if t>=2:
        t=math.factorial(t)//(2*math.factorial(t-2))
    else:
        t=0
    print(z+t)
    test-=1
        
