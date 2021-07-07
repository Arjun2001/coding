class Tree:
	def __init__(self , value):
		self.value = value
		self.left = None
		self.right = None

def constructTree(postfix):
	stack = []
	for char in postfix :
		if not isOperator(char):
			t = Tree(char)
			stack.append(t)
		else:
			t = Tree(char)
			t1 = stack.pop()
			t2 = stack.pop()
			t.right = t1
			t.left = t2
			stack.append(t)
	t = stack.pop()
	return t

def isOperator(c):
	if (c == '+' or c == '-' or c == '*'
		or c == '/' or c == '^'):
		return True
	else:
		return False

def inorder(t):
	if t is not None:
		inorder(t.left)
		print (t.value,end=' ')
		inorder(t.right)

def preorder(t):
    if t is not None:
        print(t.value, end =" ")
        preorder(t.left)
        preorder(t.right)


def evaluateExpressionTree(root): 
    if root is None: 
        return 0
    if root.left is None and root.right is None: 
        return int(root.value)  
    left_sum = evaluateExpressionTree(root.left) 
    right_sum = evaluateExpressionTree(root.right) 

    if root.value == '+':
        return left_sum + right_sum 
      
    elif root.value == '-':
        return left_sum - right_sum 
      
    elif root.value == '*':
        return left_sum * right_sum 
      
    else: 
        return left_sum / right_sum

postfix = list(input().split(' '))
r = constructTree(postfix)
print ("Infix expression is : ", end = " ")
inorder(r)
print('')
print ("Prefix expression is : ", end = " ")
preorder(r)
print('')
print(evaluateExpressionTree(r))
