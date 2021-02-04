test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    arr=[]
    for i in range(n):
        if a[i] not in arr and a[i]!=0:
            arr.append(a[i])
            count+=1
    print(count)
    test-=1
