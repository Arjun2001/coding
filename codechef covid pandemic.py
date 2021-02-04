test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    ctr=0
    start=a.index(1)+1
    for i in range(start,n):
        if (a[i]==0):
            ctr+=1
        else:
            if ctr>=5:  
                ctr=0
            else:
                flag=1
                print("NO")
                break
    if (flag==0):
        print("YES")
    test-=1
