import sys
def solve(arr,i,j):
    if i >= j:
        return 0 
    if dp[i][j] != -1:
        return dp[i][j]
    mini = 0

    for k in range(i,j,1):
        temp = solve(arr,i,k) + solve(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j])
        mini = max(mini,temp)
    dp[i][j] = mini
    return dp[i][j]



nums = [1,5]
nums = [1] + nums + [1]
dp = [[-1 for x in range(len(nums)+1)] for y in range(len(nums)+1)]
print(solve(nums,1,len(nums)-1))