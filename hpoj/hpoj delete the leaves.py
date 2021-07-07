class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def levelorder(root):
    if root is None:
        return None
    q = []
    ans = []
    q.append(root)
    while(len(q)!=0):
        node = q.pop(0)
        if node == None:
            ans.append('null')
        else:
            ans.append(node.data)
            q.append(node.left)
            q.append(node.right)
    index = 0
    fin_ans = ans
    for i in range(len(ans)-1,-1,-1):
        if ans[i] != 'null':
            index = i
            break
    for i in range(index+1):
        print(fin_ans[i],end= " ")
    print()

def createTree(arr,root,i,n):
    if i >= n:
        return
    else:
        root = Node(arr[i])
        root.left = createTree(arr,root.left,2*i+1,n)
        root.right = createTree(arr,root.right,2*i+2,n)
    return root
        
def deleteleaves(root,x):
    if (root == None):
        return None
    else:
        root.left = deleteleaves(root.left, x) 
        root.right = deleteleaves(root.right, x)
        if (root.data == x and 
            (root.left == None) and 
            (root.right == None )):
            return None
        return root

def solve():
    arr = list(input().split())
    x = input()
    n =  len(arr)
    l = n
    root = None
    root = createTree(arr,root,0,l)
    deleteleaves(root,x)
    levelorder(root)

solve()



