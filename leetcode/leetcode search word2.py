class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for c in word:
            if not node.children.get(c):
                node.children[c] = TrieNode()
            node = node.children[c]
        node.last = True
    
def dfs(board,node,i,j,temp,res):
    if node.last:
        res.append(temp)
        node.last = False
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    tmp = board[i][j]
    node = node.children.get(tmp)
    if not node:
        return
    board[i][j] = '#'
    dfs(board,node,i+1,j,temp+tmp,res)
    dfs(board,node,i-1,j,temp+tmp,res)
    dfs(board,node,i,j+1,temp+tmp,res)
    dfs(board,node,i,j-1,temp+tmp,res)
    board[i][j] = tmp

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
words = ["ABCCED"]

t = Trie()
node = t.root
for i in words:
    t.insert(i)
res = []
for i in range(len(board)):
    for j in range(len(board[0])):
        dfs(board,node,i,j,"",res)
print(res)