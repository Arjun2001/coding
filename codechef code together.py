test=int(input())
while(test):
    import math
    n,m=list(map(int,input().split()))
    group=list(map(int,input().split()))
    studpow=list(map(int,input().split()))
    grppow=list(map(int,input().split()))
    d=dict()
    for i in range(n):
        if group[i] not in d:
            d[group[i]]=[]
            d[group[i]].append(studpow[i])
        else:
            d[group[i]].append(studpow[i])
    for i in range(1,len(d)+1):
        temp=1
        d[i].sort()
        for j in d[i]:
            if math.gcd(j,grppow[i-1])==1 or (math.gcd(j,grppow[i-1])!=1 and d[i][len(d[i])-1]==j):
                temp*=j
        print(temp%grppow[i-1],'',end="")
    print('')
        
