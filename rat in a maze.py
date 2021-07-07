
def solve(maze,x,y,val):
    if x < 0 or y < 0 or x >=n or y >=n:
        return 0
    
    solve(maze,x+1,y,val)
    solve(maze,x,y+1,val)
    if maze[x][y] == 1:
        if maze[x-]
        maze[x][y] += 1
    else:
        return


n = 4
maze = [ [1, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 1, 1, 0],
             [1, 1, 1, 1] ]
solve(maze,0,0,[])
print(maze,maze[3][3])