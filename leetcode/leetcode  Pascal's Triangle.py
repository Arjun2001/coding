numRows = 5
ans = [[1]]
i = 0
while(i<numRows-1):
    temp = [1]
    for j in range(1,len(ans[i])):
        temp.append(ans[i][j]+ans[i][j-1])
    temp.append(1)
    ans.append(temp)
    i += 1
print(ans)