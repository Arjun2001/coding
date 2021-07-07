boxTypes = [[1,3],[2,2],[3,1]]
truckS = 4
boxTypes.sort(reverse=True,key=lambda x:x[1])
ans = 0
for i in boxTypes:
    temp = truckS - i[0]
    if temp>0:
        ans += i[0]*i[1]
        truckS = temp
    else:
        ans += truckS*i[1]
        break
print(ans)