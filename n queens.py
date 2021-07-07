def safe(board,row,col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board,col):
    if col >= n:
        return True
    
    for i in range(n):
        if safe(board,i,col):
            board[i][col] = 1
            if solve(board,col+1):
                return True
            board[i][col] = 0

    return False

def prinfn(board):
    arr = []
    for i in range(n):
        s = ""
        for j in range(n):
            if (board[i][j]):
                s+='Q'
            else:
                s+='.'
        arr.append(s)
    print(arr)

n = 4
board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]
if solve(board,0) == False:
    print("No solution exists")
else:
    prinfn(board)