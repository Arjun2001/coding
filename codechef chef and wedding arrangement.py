test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    dp=[0]*(n+5)
    dp[0]=0
    
    for i in range(n):
        dp[i+1]=dp[i]+k
        clash=0
        f=[0]*105
        for j in range(i,-1,-1):
            f[a[j]]+=1
            if f[a[j]]==2:
                clash+=2
            elif f[a[j]]>2:
                   clash+=1
            dp[i+1]=min(dp[i+1], dp[j]+k+clash)
    print(dp[n])
    test-=1
