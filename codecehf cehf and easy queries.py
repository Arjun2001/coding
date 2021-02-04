test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sol=0
    temp=0
    for i in range(n):
        if a[i]>=k or (temp+a[i])>=k:
            temp=temp+a[i]-k
        else:
            print(i+1)
            sol=1
            break
    if sol==0:
        days=n
        no=temp//k
        days=days+no+1
        print(days)
    test-=1
