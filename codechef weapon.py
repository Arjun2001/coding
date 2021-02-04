test=int(input())
while(test):
    n=int(input())
    ctr=0
    a=[0]*10
    for i in range(n):
        b=list(map(int,input()))
        for j in range(10):
            if a[j]==1:
                if b[j]==1:
                    a[j]=0
            else:
                a[j]=b[j]
    for i in a:
        if i==1:
            ctr+=1
    print(ctr)
    test-=1
            
