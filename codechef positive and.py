def countones(n):
    count=0
    while n>0:
        if n%2!=0:
            count+=1
        n=n//2
    return count

test=int(input())
while(test):
    test-=1
    n=int(input())
    three="1 3 2"
    five="2 3 1 5 4"
    count=countones(n)
    if n==3:
        print(three)
    elif n==5:
        print(five)
    elif n==1:
        print("1")
    elif count==1:
        print("-1")
    else:
        nextnum=0
        print(five,end=" ")
        for i in range(6,n+1):
            num=countones(i)
            if num==1:
                nextnum=i+1
                print(i+1, i, end=" ")
            elif i!=nextnum:
                print(i,end=" ")
        print('')
    
