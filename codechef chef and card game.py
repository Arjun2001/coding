test=int(input())
while(test):
    n=int(input())
    chef=motu=0
    for i in range(n):
        temp1=temp2=0
        a=list(map(int,input().split()))
        while(a[0]>0 or a[1]>0):
            temp1=temp1+(a[0]%10)
            temp2=temp2+(a[1]%10)
            a[0]=int(a[0]/10)
            a[1]=int(a[1]/10)
        if(temp1>temp2):
            chef+=1
        elif temp1<temp2:
            motu+=1
        else:
            chef+=1
            motu+=1
    if(chef>motu):
        print('0',chef)
    elif (chef<motu):
        print('1',motu)
    else:
        print('2',chef)
    test-=1
            
