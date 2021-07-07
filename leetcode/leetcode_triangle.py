import copy
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
l = len(triangle)
dp = copy.deepcopy(triangle[-1])
for row in range(l-2,-1,-1):
    for j in range(row+1):
        dp[j] = min(dp[j],dp[j+1]) + triangle[row][j]
print(dp[0])