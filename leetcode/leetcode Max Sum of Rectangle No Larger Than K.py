matrix = [[1,0,1],[0,-2,3]]
k = 2
row = len(matrix)
column = len(matrix[0])

# calculating the prefix sum of all the rows of a matrix
for i in range(row):
    for j in range(1,column):
        matrix[i][j] += matrix[i][j-1]
ans = 0
for i in range(column):
    for j in range(i,column):
        sums,mp = 0,{}
        for k in range(row):
            sums += matrix[k][j]
            if i > 0:
                sums -= matrix[k][i-1]
            if sums - k in mp:
                ans += 

