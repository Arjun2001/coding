def search(arr , st, en, key):
    mid = st+ (en-st)//2
    if key < arr[mid]:
        if key >= arr[mid-1] or st == en or mid == st:
            arr.insert(mid,key)
            return mid
        else:
            return search(arr, st, mid-1, key)
    else:
        if st == en:
            arr.append(key)
            return len(arr)-1
        else:
            return search(arr, mid+1, en, key)

n =  int(input())
a = list(map(int,input().split()))
arr = [a[0]]
ans = 0
for i in range(1,n):
    ans += (len(arr)-search(arr, 0, len(arr)-1, a[i]))
print(ans)
