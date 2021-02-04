test=int(input())
while(test):
    n=int(input())
    s=[]
    p=[]
    v=[]
    ans=0
    for i in range(n):
        temp=list(map(int,input().split()))
        s.append(temp[0])
        p.append(temp[1])
        v.append(temp[2])
        ans=max(ans,int(p[i]/(s[i]+1))*v[i])
    print(ans)
    test-=1
