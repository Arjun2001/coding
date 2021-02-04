test=int(input())
while(test):
    n,m=list(map(int,input().split()))
    f=list(map(int,input().split()))
    p=list(map(int,input().split()))
    mini=100000000
    for i in range(m):
        exist=0
        mins=0
        for j in range(n):
            if f[j]==(i+1):
                exist=1
                mins+=p[j]
        if mins<mini and exist:
            mini=mins
    print(mini)
    test-=1
