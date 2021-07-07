nums = [0,1,2,3,4,5,6,7,8,9]
s = set(nums)
ans = 0
for num in nums:
    j = 1
    if num + j not in s:
        while num - j in s:
            j += 1
        ans = max(ans,j)
print(ans)