def search(arr, st, en, key): 
    if st>en:
        return -1
    else:
        mid = st + (en-st)//2
        print("index = ",mid)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return search(arr,st,mid-1,key)
        else:
            return search(arr,mid+1,en,key)

tc = int(input())
a = list(map(int,input().split()))
for i in range(tc):
    key = int(input())
    print(search(a,0,len(a)-1,key))
