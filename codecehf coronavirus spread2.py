def recurse(i,a,box):
    if i not in box:
        box.append(i)
        for j in range(len(a)):
            if i>j:
                if a[i]<a[j] and (j not in box):
                    recurse(j,a,box)
            else:
                if a[i]>a[j] and (j not in box):
                    recurse(j,a,box)
        return len(box)
    else:
        return 0
        


test=int(input())
while(test):
    test-=1
    n=int(input())
    a=list(map(int,input().split()))
    arr=[0]*n
    for i in range(n):
        box=[]
        arr[i]=recurse(i,a,box)
    print(min(arr),max(arr))
            
