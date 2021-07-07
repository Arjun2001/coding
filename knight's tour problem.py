def printfn(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end = " ")
        print()

def safe(board,x,y):
    if x >=0 and y>=0 and x<n and y<n and board[x][y] == -1:
        return True
    else:
        return False

def findPath(board,n,cur_x,cur_y,x_pos,y_pos,index):
    if index == n*n:
        return True
    
    for i in range(n):
        new_x = x_pos[i] + cur_x
        new_y = y_pos[i] + cur_y
        if safe(board,new_x,new_y):
            board[new_x][new_y] = index
            if(findPath(board,n,new_x,new_y,x_pos,y_pos,index+1)):
                return True
            board[new_x][new_y] = -1

    return False


n = 8

board = [[-1 for x in range(n)] for y in range(n)]
board[0][0] = 0

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
pointer = 1
if (findPath(board,n,0,0,move_x,move_y,pointer)):
    printfn(board)
else:
    print("No Solution Exist")