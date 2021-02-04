test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ans=''
    for i in range(n):
        if a[i]%k == 0:
            ans+='1'
        else:
            ans+='0'
    print(ans)
    test-=1
