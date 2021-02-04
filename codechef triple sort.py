test=int(input())
while(test):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    arr=[]
    dummyarr=[]
    temp=[]
    i=index=0
    while index!=n:
        found=0
        if a[i] in dummyarr:
            found=1
        if found==0:
            temp.append(a[i])
            dummyarr.append(a[i])
            i=a[i]-1
            if i==index:
                index+=1
        else:
            if(len(temp)>=2):
                arr.append(temp)
            temp=[]
            index+=1
            i=index
    evecount=0
    seq=[]
    oned=-1
    twod=-1
    for i in range(len(arr)):
        if (len(arr[i])%2==0):
            evecount+=1
    if(evecount%2!=0):
        print('-1')
    else:
        for i in range(len(arr)):
            if(len(arr[i])%2!=0):
                for j in range(1,len(arr[i]),2):
                    temp3=[]
                    one=arr[i][j-1]
                    two=arr[i][j]   
                    three=arr[i][j+1]
                    temp3.append(a.index(one)+1)
                    temp3.append(a.index(two)+1)
                    temp3.append(a.index(three)+1)
                    seq.append(temp3)
                    a[a.index(two)]=one
                    a[a.index(three)]=two
                    a[a.index(one)]=three
            else:
                j=1
                temp3=[]
                for j in range(1,len(arr[i])-2,2):
                    temp3=[]
                    one=arr[i][j-1]
                    two=arr[i][j]
                    three=arr[i][j+1]
                    temp3.append(a.index(one)+1)
                    temp3.append(a.index(two)+1)
                    temp3.append(a.index(three)+1)
                    seq.append(temp3)
                    a[a.index(two)]=one
                    a[a.index(three)]=two
                    a[a.index(one)]=three
                one=arr[i][j-1]
                two=arr[i][j]
                if(oned==-1):
                    oned=a.index(one)
                    twod=a.index(two)
                    print(oned,twod,"dfdg")
                else:
                    temp3.append(a.index(oned)+1)
                    temp3.append(a.index(twod)+1)
                    temp3.append(a.index(one)+1)
                    print(temp3)
                    seq.append(temp3)
                    temp3=[]
                    temp3.append(a.index(twod)+1)
                    temp3.append(a.index(one)+1)
                    temp3.append(a.index(two)+1)
                    seq.append(temp3)
                    oned=-1
                a[a.index(one)]=two
                a[a.index(two)]=one
        if (len(seq)<=k):
            print(len(seq))
            for k in range(len(seq)):
                print(seq[k][0],seq[k][1],seq[k][2])
        else:
            print('-1')
    test-=1
            
