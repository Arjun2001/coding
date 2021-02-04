test=int(input())
while(test):
    a=list(map(int,input().split()))
    maximum=0
    for i in range(a[2],a[3]):
        maximum=max((a[0]&i)*(a[1]&i),maximum)
    print(maximum)
    test-=1
