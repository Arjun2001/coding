test=int(input())
while(test):
    n=int(input())
    a=[]
    for i in range(n):
        temp=int(input())
        a.append(temp)
    count=0
    a.sort()
    for i in range(n-1):
        if a[i]<a[i+1]:
            count+=1
    print(n-count)
    test-=1
