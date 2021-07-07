def safe(board,x,y,n):
    for i in range(y):
        if board[x][i] == 1:
            return False
    for i,j in zip(range(x,-1,-1),range(y,-1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(x,n,1),range(y,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board,n,col):
    if col >= n:
        global ans
        ans += 1
    for i in range(n):
        if (safe(board,i,col,n)):
            board[i][col] = 1
            if (solve(board,n,col+1)):
                return True
            board[i][col] = 0
    return False


n = 4
ans = 0
board = [[0 for x in range(n)] for y in range(n)]
solve(board,n,0)
print(ans)