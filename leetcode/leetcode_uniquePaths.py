def recur(arr,i,j,dp):
    ans = 0
    if i >= len(arr) or j >= len(arr[0]):
        return 0
    if arr[i][j] == 1:
        return 0
    if i == len(arr)-1 and j == len(arr[0])-1:
        return 1
    if dp[i][j]:
        return dp[i][j]
    dp[i][j] = recur(arr,i+1,j,dp) + recur(arr,i,j+1,dp)
    return dp[i][j]

grid = [[0,0,0],[0,1,0],[0,0,0]]
dp = [[0]* len(grid[0]) for i in range(len(grid))]
print(recur(grid,0,0,dp))