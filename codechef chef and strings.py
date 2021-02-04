test=int(input())
while(test):
    n=int(input())
    s=list(map(int,input().split()))
    ans=0
    for i in range(n-1):
        ans=ans+abs(s[i]-s[i+1])-1
    print(ans)
    test-=1
