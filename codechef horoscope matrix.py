def search(a):
    arr = []
    for i in range(n-1, -1, -1):
        x = i
        y = 0
        val = a[x][y]
        arr.append([x,y,val])
        while ( x < n):
            if a[x][y] != val:
                arr.pop()
                break
            x += 1
            y += 1
    for i in range(1,m):
        x = 0
        y = i
        val = a[x][y]
        arr.append([x,y,val])
        while(y < m):
            if a[x][y] != val:
                arr.pop()
                break
            x += 1
            y += 1
    return arr

            
for _ in range(int(input())):
    n,m = map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    arr = search(a)
    print(arr)
    q = int(input())
    for i in range(q):
        a = list(map(int,input().split()))
        if a in arr:
            print(len(arr))
    
