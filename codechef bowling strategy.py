test=int(input())
while(test):
    test-=1
    n,k,l=list(map(int,input().split()))
    if ((k*l) < n):
        print('-1')
    else:
        count=0
        i=1
        a=[0]*(k+1)
        while (count!=n):
            if i==k+1:
                i=1
            if a[i]<=l:
                print(i,end=" ")
                count+=1
            i+=1
        print('')
    
                
