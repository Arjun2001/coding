test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a1=list(map(int,input().split()))
    a2=[0]*len(a1)
    temp1=sorted(a1)
    temp2=sorted(a1,reverse=True)
    for i in range(0,k):
        b=[]
        for j in range(i,n,k):
            b.append(a1[j])
        b.sort()
        ind=0
        
        for m in range(i,n,k):
            a1[m]=b[ind]
            ind+=1
        b.sort(reverse=True)
        ind=0
        for m in range(i,n,k):
            a2[m]=b[ind]
            ind+=1
    if(temp1==a1 or temp2==a2):
        print('yes')
    else:
        print('no')
    test-=1
