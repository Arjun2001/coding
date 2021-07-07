a = list(map(int,input().split()))
s = sum(a)
l = len(a)
dp = [[0 for i in range(s+1)] for j in range(l+1)]

for i in range(l+1):
    dp[i][0] = True

for i in range(1,s+1):
    dp[0][i] = False

for i in range(1,l+1):
    for j in range(1,s+1):
        dp[i][j] = dp[i-1][j]
        if j >= a[i-1]:
            dp[i][j] |= dp[i][j-a[i-1]]

for j in range(s//2,-1, -1):
    if dp[l][j] == True:
        diff = s - (2*j)
        break
print(diff)

