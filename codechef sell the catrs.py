test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=ctr=0
    for i in range(n-1,-1,-1):
        ctr+=1
        if(a[i]!=0 and (a[i]-ctr+1)>0):
            ans=ans+(a[i]-ctr+1)
    print(ans%1000000007)
    test-=1
