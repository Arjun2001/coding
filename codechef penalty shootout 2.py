test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input()))
    asc=bsc=0
    are=bre=n
    flag=0
    for i in range(0,len(a)):
        if(a[i]==1):
            if(i%2==0):
                asc+=1
            else:
                bsc+=1
        if(i%2==0):
            are-=1
        else:
            bre-=1
        diff=(asc-bsc)
        diff1=(bsc-asc)
        if(diff>bre) or(diff1>are):
            print(i+1)
            flag=1
            break
    if(flag==0):
        print(n+n)
    test-=1
