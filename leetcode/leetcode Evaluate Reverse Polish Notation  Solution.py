def solve(b,a,i):
    print(a,b)
    if i == "+" :
        return int(a) + int(b)
    if i == '-' :
        return int(a) - int(b)
    if i == '*' :
        return int(a) * int(b)
    if i == '/':
        return int(int(a) / int(b))



tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []

for i in tokens:
    if i == "+" or i == '-' or i == '*' or i == '/':
        res = solve(stack.pop(),stack.pop(),i)
        stack.append(str(res))
    else:
        stack.append(i)
print(stack[0])
