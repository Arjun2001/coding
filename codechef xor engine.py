test=int(input())
while(test):
    n,q=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in range(q):
        q1=int(input())
        for j in range(n):
            a[j]=a[j]^q1
            temp=a[j]^(a[j]>>1)
            temp=temp^(a[j]>>2)
            temp=temp^(a[j]>>4)
            temp=temp^(a[j]>>8)
            temp=temp^(a[j]>>16)
            if temp&1:
                a[j]=1
            else:
                a[j]=0
        count=0
        for j in range(n):
            if a[j]==0:
                count+=1
        print(count,n-count)
    test-=1
            
