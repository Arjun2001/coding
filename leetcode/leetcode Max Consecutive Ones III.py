nums = [1,1,1,0,0,0,1,1,1,1,0] 
k = 3
tempk = k
i = j = count = maxi = 0
for j in range(len(nums)):
    if nums[j] == 0:
        if k == 0:
            while nums[i] != 0:
                i += 1
            i += 1
        else:
            k -= 1
    
    print(i,j,k)
    maxi = max(maxi,(j-i+1))
print(maxi)
    