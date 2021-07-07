class newNode:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None

def buildUtil(In, post, inStrt, inEnd, pIndex):
    if (inStrt > inEnd): 
        return None
    node = newNode(post[pIndex[0]]) 
    pIndex[0] -= 1
    if (inStrt == inEnd): 
        return node
    else:
        iIndex = search(In, inStrt, inEnd, node.data)
        node.right = buildUtil(In, post, iIndex + 1,inEnd, pIndex) 
        node.left = buildUtil(In, post, inStrt,iIndex - 1, pIndex) 
        return node

def buildTree(In, post, n):
    pIndex = [n - 1] 
    return buildUtil(In, post, 0, n - 1, pIndex)

def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value): 
            break
    return i

min_sum_ref = 0
target_leaf_ref = None

def maxSumPath( Node):
    global min_sum_ref 
    global target_leaf_ref
    min_leaf = []
    if (Node == None):
        return 0
    target_leaf_ref = None
    min_sum_ref = 10000000000
    getTargetLeaf(Node, 0)
    return target_leaf_ref.data

def getTargetLeaf(Node, curr_sum): 
    global min_sum_ref 
    global target_leaf_ref
    global sum_arr
    if (Node == None): 
        return
    curr_sum = curr_sum + Node.data 
    if (Node.left == None and Node.right == None):
        if (curr_sum < min_sum_ref):
            min_sum_ref = curr_sum 
            target_leaf_ref = Node
        if (curr_sum == min_sum_ref):
            if target_leaf_ref.data > Node.data :
                target_leaf_ref = Node
    getTargetLeaf(Node.left, curr_sum) 
    getTargetLeaf(Node.right, curr_sum)


for _ in range(int(input())):
    In = list(map(int,input().split()))
    post = list(map(int,input().split()))
    n = len(In)
    root = buildTree(In, post, n)
    print(maxSumPath(root))