test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    temp=0
    check=0
    a=list(map(int,input().split()))
    for i in range(n):
        temp=a[i]-k
        if temp>0 and i!=n-1:
            a[i+1]+=temp
        elif temp<0:
            print("NO "+str(i+1))
            check=1
            break;
    if check==0:
        print("YES")
    test-=1
