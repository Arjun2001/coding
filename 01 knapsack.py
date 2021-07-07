def knap(weight,val,w,n,dp):
    if w == 0 or n == 0:
        return 0
    if dp[n][w] != -1:
        print("hi")
        return dp[n][w]
    if weight[n-1] <= w:
        dp[n][w] = max(val[n-1] + knap(weight,val,w-weight[n-1],n-1,dp), knap(weight,val,w,n-1,dp))
    else:
        dp[n][w] = knap(weight,val,w,n-1,dp)
    return dp[n][w]
        


weight = [1,3,4,5,2,6,7]
val = [1,4,5,7,2,4,4]  
w = 10
dp = [[-1 for x in range(w+2)] for y in range(len(val)+2)]   

print(knap(weight,val,w,len(val),dp))