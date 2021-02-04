def route(arr, d):
    for i in arr:
        if len(i)==3:
            if d >= i[1]-1:
                d += i[2]
        else:
            d -= i[1]
        if d < 0:
            return False
    return True
            
            
for _ in range(int(input())):
    end = int(input())
    a = list(map(int,input().split()))
    dishes = a[0]
    a = a[1:]
    b = list(map(int,input().split()))
    priest = b[0]
    b = b[1:]
    arr = []
    st = en = 0
    for i in range(0,2*dishes,2):
        arr.append([a[i],a[i+1]])
        en += a[i+1]
    for i in range(0,3*priest,3):
        arr.append([b[i],b[i+1],b[i+2]])
    arr.sort()
    while st <= en:
        mid = st+(en-st)//2
        if route(arr, mid):
            en = mid - 1
            var = 0
        else:
            st = mid + 1
            var = 1
    print(mid + var+ 1)
    
    
    
