test=int(input())
while(test):
    n=int(input())
    a=input().split()   
    d=dict()
    for x in range(1,11):
        d[str(x)]=0
    for x in range(n):
        d[a[x]]+=1
    ans=[0]*(10005)
    for i in range(1,11):
        if d[str(i)]!=0:
            ans[d[str(i)]]+=1
    count=0
    for i in range(len(ans)):
        if ans[i]>count:
            count=ans[i]
            index=i
    print(index)
    test-=1
