n=int(input())
a=list(map(int,input().split()))
depth=depthst=inner=innerst=0
stack=[]
for i in range(n):
    if a[i]==1:
        stack.append(1)
        if(len(stack)==1):
            temp=0
        if len(stack)>depth:
            depth=len(stack)
            depthst=i+1
        temp+=1
    else:
        temp+=1
        stack.pop()
        if temp>inner:
            inner = temp
            innerst=i+2-inner
        if(len(stack)==0):
            temp=0
print(depth,depthst,inner,innerst)
        
        
            
    
