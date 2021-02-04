test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]&a[j]==a[i]:
                count+=1
    print(count)
    test-=1
