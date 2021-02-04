test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    freq=[0]*(k+5)
    freq[0]=1
    maxseq=distinct=0
    i=0
    j=0
    while(1):
        while(j<n and distinct<k):
            if (freq[a[j]] == 0):
                distinct+=1
            freq[a[j]]+=1
            if distinct<k:
                maxseq=max(maxseq, j-i+1)
            j+=1
        if j==n:
            break
        while(i<=(j-1) and distinct==k):
            if ( freq[a[i]] == 1):
                distinct-=1
            freq[a[i]]-=1
            i+=1
    print(maxseq)
    test-=1
