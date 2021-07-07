
def solve(i,j):
    if i < 0 or j < 0 or i >=n or j >= m or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    return 1 + solve(i-1,j) + solve(i,j-1) + solve(i+1,j) + solve(i,j+1)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
n = len(grid)
m = len(grid[0])
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            ans = max(ans,solve(i,j))
print(ans)
