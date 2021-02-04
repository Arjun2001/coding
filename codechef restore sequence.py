test = int(input())
prime = [1]*(1299720)
p = 2
while (p*p < 1299720):
    if prime[p]==1:
        for i in range(p*p,1299720,p):
            if prime[i]==1:
                prime[i] = 0
    p+=1
ans=[]
for i in range(2,1299720):
    if prime[i]:
        ans.append(i)
while(test):
    test -= 1
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1,n+1):
        if a[i-1] == i:
            print(ans[i-1], end = ' ')
        else:
            print(ans[a[i-1]-1], end = ' ')
    print('')
