test=int(input())
while(test):
    c,r=list(map(int,input().split()))
    'this is only for chef score'
    temp=int(c/9)
    if temp==0:
        chef=1
    else:
        chef=temp
        if (c%9)!=0:
            chef+=1
    'end for chef'
    'start for friend'
    temp1=int(r/9)
    if temp1==0:
        friend=1
    else:
        friend=temp1
        if (r%9)!=0:
            friend+=1
    'end of friend'
    if chef<friend:
        print("0",chef)
    elif chef>friend:
        print('1',friend)
    else:
        print('1',chef)
    test-=1
    
            
