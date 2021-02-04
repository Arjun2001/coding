test=int(input())
while(test):
    a=list(input())
    b=[]
    ans=0
    temp=0
    for i in range(len(a)):
        if(a[i]=='<'):
            b.append('<')
        else:
            if(len(b)==0):
                break
            b.pop()
            temp+=2
            if len(b)==0:
                ans+=temp
                temp=0
    print(ans)
    test-=1
        
        
    
