test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    tot=count=0
    for i in range(n):
        tot+=a[i]
        if tot>k and a[i]>k:
            count=0
            break
        elif tot>k:
            count+=1
            tot=a[i]
        elif tot==k:
            count+=1
            tot=0
        if i==n-1 and tot<k and tot!=0:
            count+=1
            tot=0
    if count==0:
        print('-1')
    else:
        print(count)
    test-=1
