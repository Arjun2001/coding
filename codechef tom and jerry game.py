import math
test=int(input())
while(test):
    ts=int(input())
    lg=int(math.log(ts,2))
    print(lg)
    lg=int(math.pow(2,lg))
    if ts==1 or lg==ts:
        print("0")
    elif ts%2==0:
        temp=0
        temp1=int(math.log(ts,2))
        while(ts%2==0):
            temp+=1
            ts=ts//2
        print(temp1-temp)
    else:
        print(ts//2)
    test-=1
