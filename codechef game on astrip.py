test=int(input())
while(test):
    n=int(input())
    a=list(map(int,input().split()))
    temp=0
    count = []
    for i in range(n):
        if a[i]==0:
            temp+=1
        else:
            count.append(temp)
            temp=0
    count.sort(reverse=True)
    if count[0]%2==1 and count[1]<((count[0]+1)//2):
        print('Yes')
    else:
        print('No')
    test-=1
