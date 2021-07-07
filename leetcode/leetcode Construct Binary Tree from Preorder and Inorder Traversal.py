class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def build(inorder,preorder,inStart,inEnd):
    
    global preIndex,mp
    print(inorder,preorder,inStart,inEnd,preIndex)
    if inStart > inEnd:
        return None
    cur = preorder[preIndex]
    tNode = Node(cur)
    preIndex += 1

    if inStart == inEnd:
        return tNode
    
    index = mp[cur]
    tNode.left = build(inorder,preorder,inStart,index-1)
    tNode.right = build(inorder,preorder,index+1,inEnd)
    return tNode


inorder = [ -1]
preorder = [ -1]

mp = {}
preIndex = 0
n = len(inorder)
for i in range(n):
    mp[inorder[i]] = i
node = build(inorder,preorder,0,n-1)
print(node.data,node.right,node.left)