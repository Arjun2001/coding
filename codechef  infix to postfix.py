test=int(input())
while(test):
    n=int(input())
    a=list(input())
    a.insert(0,"(")
    a.append(")")
    stack=[]
    for i in range(len(a)):
        if(a[i]!=')'):
            stack.append(a[i])
        else:
            temp=''
            temp1=[]
            while(temp!='('):
                temp=stack.pop()
                if(temp=='('):
                    break
                if temp=='+' or temp=='-' or temp=='/' or temp=='*' or temp=='^':
                    temp1.append(temp)
                else:
                    temp1.insert(0,temp)
            temp1="".join(map(str,temp1))
            stack.append(temp1)
    while(len(stack)!=1):
        temp=stack.pop()
        if(temp=='('):
            break
        if temp=='+' or temp=='-' or temp=='/' or temp=='*' or temp=='^':
            temp1.append(temp)
        else:
            temp1.insert(0,temp)
    print(stack[0])    
    test-=1
