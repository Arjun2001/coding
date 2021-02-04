test=int(input())
while(test):
    n=int(input())
    larr=[]
    rarr=[]
    for i in range((4*n)-1):
        a,b=list(map(int,input().split()))
        if a not in larr:
            larr.append(a)
        else:
            larr.remove(a)
        if b not in rarr:
            rarr.append(b)
        else:
            rarr.remove(b)
    print(larr[0],rarr[0])
    test-=1
        
