nums = [1,10,2,9]
nums.sort()
left = 0
right = len(nums)-1
s = 0
while(left < right):
    s += nums[right] - nums[left]
    right -= 1
    left += 1
print(s)
