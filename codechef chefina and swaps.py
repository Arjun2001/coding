test=int(input())
while(test):
    simply=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    afreq=[]
    bfreq=[]
    for i in range(n):
        afreq.append(a.count(a[i]))
        bfreq.append(b.count(b[i]))
    check=count=0
    for i in range(n):
        if a[i] in b:
            temp=afreq[i]+bfreq[i]
            if temp%2!=0:
                check=1
                break
            else:
                if afreq[i]!=bfreq[i]:
                    count=count+int(abs(afreq[i]-bfreq[i])/2)
        else:
            if afreq[i]%2!=0:
                check=1
                break
        if b[i] in a:
            temp=bfreq[i]+afreq[i]
            if temp%2!=0:
                check=1
                break
        else:
            if bfreq[i]%2!=0:
                check=1
                break
    if check==1:
        print('-1')
