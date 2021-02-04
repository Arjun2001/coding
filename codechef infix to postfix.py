test=int(input())
while(test):
    n=int(input())
    a=input()
    store={'(' :0, '+':1, '-':1, '*':2, '/':2, '^':3}
    stack=[]
    for i in range(n):
        temp=a[i]
        if temp!=')':
            if temp == '(':
                stack.append(temp)
            elif temp in store:
                if len(stack)>0 and store[temp]>store[stack[-1]]:
                    stack.append(temp)
                else:
                    while len(stack)>0 and stack[-1]!='(' and store[temp]<=store[stack[-1]]:
                        print(stack.pop(),end="")
                    stack.append(temp)
            else:
                print(temp, end ="")
        else:
            while len(stack)>0 and stack[-1]!='(':
                print(stack.pop(), end="")
            if len(stack)>0:
                stack.pop()
    while len(stack)>0:
        print(stack.pop(), end="")
    print("")
    test-=1
