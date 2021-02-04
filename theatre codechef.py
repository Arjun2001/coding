test=int(input())
so_far=0
while(test):
    l=m=p=o=[0]*4
    temp=[]
    n=int(input())
    now=0
    while(n):
        a=input().split()
        if a[0]=="A" and a[1]=="12":
            l[0]+=1
        elif a[0]=="B" and a[1]=="12":
            m[0]+=1
        elif a[0]=="C" and a[1]=="12":
            p[0]+=1
        elif a[0]=="D" and a[1]=="12":
            o[0]+=1
        elif a[0]=="A" and a[1]=="3":
            l[1]+=1
        elif a[0]=="B" and a[1]=="3":
            m[1]+=1
        elif a[0]=="C" and a[1]=="3":
            p[1]+=1
        elif a[0]=="D" and a[1]=="3":
            o[1]+=1
        elif a[0]=="A" and a[1]=="6":
            l[2]+=1
        elif a[0]=="B" and a[1]=="6":
            m[2]+=1
        elif a[0]=="C" and a[1]=="6":
            p[2]+=1
        elif a[0]=="D" and a[1]=="6":
            o[2]+=1
        elif a[0]=="A" and a[1]=="9":
            l[3]+=1
        elif a[0]=="B" and a[1]=="9":
            m[3]+=1
        elif a[0]=="C" and a[1]=="9":
            p[3]+=1
        else:
            o[3]+=1
        n-=1
    ans=[0]*4
    temp.append(l.index(max(l)))
    ans[0]=max(l)
    while (m.index(max(m))) in temp:
        m[m.index(max(m))]=0
    temp.append(m.index(max(m)))
    ans[1]=max(m)
    while (p.index(max(p))) in temp:
        p[p.index(max(p))]=0
    temp.append(p.index(max(p)))
    ans[2]=max(p)
    while (o.index(max(o))) in temp:
        o[o.index(max(o))]=0
    temp.append(o.index(max(o)))
    ans[3]=max(o)
    tk=100
    print(ans,l,m,p,o)
    for i in range(4):
          now+=(max(ans)*tk)
          tk-=25
          ans[ans.index(max(ans))]=0
    print(now)
    so_far+=now
    test-=1
print(so_far)
