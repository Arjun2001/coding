def freq(q,item):
        if q.count(q[item])==1:
            return 0
        else:
            dist=0
            for j in range(item-1,-1,-1):
                dist+=1
                if q[j]==q[item]:
                    return dist

test=int(input())
while(test):
    n=int(input())
    a=[-1]*129
    a[0]=0
    for i in range(n-1):
        a[i+1]=freq(a,i)
    print(a.count(a[n-1]))
    test-=1

