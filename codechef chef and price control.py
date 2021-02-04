test=int(input())
while(test):
    ans=0
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(n):
        if(a[i]>=k):
            ans=ans+(a[i]-k)
    print(ans)
    test-=1
