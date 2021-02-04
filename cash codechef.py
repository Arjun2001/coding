test=int(input())
while(test):
    n,k=input().split()
    a=input().split()
    bal=0
    rem=0
    for i in a:
        if int(i)%int(k)!=0:
            rem+=(int(i)%int(k))
    bal=rem%7
    print(bal)
    test-=1
