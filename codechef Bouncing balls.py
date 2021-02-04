import math
test=int(input())
while(test):
    m=int(input())
    ctr=0
    while(m>0):
        temp=int(math.log(m,2))
        m-=int(math.pow(2,temp))
        ctr+=1
    print(ctr-1)
    test-=1
