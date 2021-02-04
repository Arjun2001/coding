test=int(input())
while(test):
    test-=1
    n,x,p,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    replacement=k-1
    destination=p-1
    arr.sort()
    count=0
    if replacement==destination:
        if arr[replacement]>x:
            for i in range(replacement,-1,-1):
                if arr[i]>x:
                    count+=1
            print(count)
        elif arr[replacement]<x:
            for i in range(replacement,n):
                if arr[i]<x:
                    count+=1
            print(count)
        else:
            print('0')
    elif replacement>destination:
        if arr[destination]>x:
            for i in range(destination,-1,-1):
                if arr[i]>x:
                    count+=1
            print(count)
        elif arr[destination]==x:
            print('0')
        else:
            print('-1')
    else:
        if arr[destination]<x:
            for i in range(destination,n):
                if arr[i]<x:
                    count+=1
            print(count)
        elif arr[destination]==x:
            print('0')
        else:
            print('-1')
