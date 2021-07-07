nums = [5,2,1,2,5,2,1,2,5]
j = 0
arr = set()
temp = ans =  0
for i in range(len(nums)):
    while(nums[i] in arr):
        temp -= nums[j]
        arr.remove(nums[j])
        j += 1
    temp += nums[i]
    arr.add(nums[i])
    ans = max(ans,temp)

print(ans)