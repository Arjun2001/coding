class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def construct(root,arr,i,n):
    if i < n:
        if arr[i] == "null":
            return
        else:
            temp = Node(arr[i])
        root = temp
        root.left = construct(root.left,arr,2*i+1,n)
        root.right = construct(root.right,arr,2*i+2,n)
    return root

def levelorder(root):
    q = []
    q.append(root)
    while len(q) != 0:
        temp = q.pop(0)
        if temp is not None:
            print(temp.data,end = " ")
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

arr = [3,9,20,"null","null",15,7]
root = None
root = construct(root,arr,0,len(arr))
levelorder(root)
print()