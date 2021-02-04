test=int(input())
while(test):
    test-=1
    n=int(input())
    a=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        a.append(temp)
    count=0
    temp=[]
    for i in range(1,n):
        if a[0][i]==(i+1):
            temp.append(1)
        else:
            temp.append(0)
    length=len(temp)
    for i in range(length-1):
        if temp[i]!=temp[i+1]:
            a[i]=a[i+1]
            count+=1
    if temp[length-1]==0:
        count+=1
    print(count)
