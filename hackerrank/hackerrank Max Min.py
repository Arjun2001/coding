import sys
arr = [10,100,300,200,1000,20,30]
k = 3
arr.sort()
ans = sys.maxsize
for i in range(len(arr)-k+1):
    ans = min(ans,arr[i+k-1] - arr [i])
print(ans)