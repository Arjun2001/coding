n = 8
k = 6
MOD = 10**9+7
dp = [[0 for x in range(k+1)] for y in range(n+1)]
for i in range(0,n+1):
    dp[i][0] = 1
for i in range(1,n+1):
    for j in range(1,k+1):
        print(i,j,k-i)
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%MOD
        if j-i >= 0:
            dp[i][j] -= (dp[i-1][j-i] + MOD)%MOD
print(dp[n][k],dp)
