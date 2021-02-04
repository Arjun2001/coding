test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ans=10**9
    checked=0
    for i in range(n):
        if k%a[i]==0:
            temp = int(k/a[i])
            checked=1
            if temp<ans:
                ans=a[i]
    if checked==0:
        print('-1')
    else:
        print(ans)
    test-=1
            
