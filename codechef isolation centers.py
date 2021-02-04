test=int(input())
store='abcdefghijklmnopqrstuvwxyz'
while(test):
    n,q=list(map(int,input().split()))
    a=list(input())
    arr=[0]*26
    for i in range(n):
        arr[store.index(a[i])]+=1
    while(q):
        q1=int(input())
        ans=0
        for i in range(len(arr)):
            if(arr[i]>q1):
                ans=ans+(arr[i]-q1)
        print(ans)
        q-=1
    test-=1
