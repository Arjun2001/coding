test=int(input())
while(test):
    n=int(input())
    a=list(input().split())
    a.sort()
    b=list(input().split())
    b.sort()
    ans=0
    for i in range(n):
        if int(a[i])<int(b[i]):
            ans+=int(a[i])
        else:
            ans+=int(b[i])
    print(ans)
    test-=1
