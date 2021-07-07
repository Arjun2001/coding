nums = [3,1,6,5,2,7,5,6,1,3,4,6]
left = 4
right = 6
ans, low, mid = 0, 0, 0
for num in nums:
    if num > right: mid = 0
    else:
        mid += 1
        ans += mid
    if num >= left: low = 0
    else:
        low += 1
        ans -= low
    print(mid,low,ans)
print(ans)