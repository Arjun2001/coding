def search(a,i,j,ele):
    if i > j:
        return -1
    mid = (i+j)//2
    print(mid)
    if a[mid] == ele:
        return mid
    elif a[mid] < ele:
        return search(a,mid+1,j,ele)
    else:
        return search(a,i,mid-1,ele)

arr = [1,2,2,7,8,9]
temp(search(arr,0,len(arr)-1,3))
if temp = -1:
    print([-1,-1])
else:
    i = j  = temp
