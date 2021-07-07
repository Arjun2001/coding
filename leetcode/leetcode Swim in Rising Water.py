def solve(arr,litres,i,j,visited,row,column):
    print(litres,i,j,visited,row,column)
    visited[i][j] = 1
    if i == row-1 and column == column-1:
        return litres
    mini = 51
    new_x,new_y = 0,0
    # down
    if i+1 < row and not visited[i+1][j]:
        if arr[i+1][j] < mini:
            mini = arr[i+1][j]
            new_x = i+1
            new_y = j
    # up
    if i-1 <= 0 and not visited[i-1][j]:
        if arr[i-1][j] < mini:
            mini = arr[i-1][j]
            new_x = i-1
            new_y = j
    # left
    if j-1 <= 0 and not visited[i][j-1]:
        if arr[i][j-1] < mini:
            mini = arr[i][j-1]
            new_x = i
            new_y = j - 1
    # right
    if j+1 < column and not visited[i][j+1]:
        if arr[i][j+1] < mini:
            mini = arr[i][j+1]
            new_x = i
            new_y = j+1
    if mini < arr[i][j]:
        lit = 0
    else:
        lit = mini - arr[i][j]
    return solve(arr,litres+mini,new_x,new_y,visited,row,column)
    

arr = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
row = len(arr)
column = len(arr[0])
visited = [[0 for x in range(column)] for y in range(row)]
print(solve(arr,0,0,0,visited,row,column))