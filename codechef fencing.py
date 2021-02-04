tc = int(input())
for i in range(tc):
    n, m , k = map(int,input().split())
    arr = set()
    value = 4*k
    for j in range(k):
        r, c = map(int,input().split())
        arr.add((r,c))
        if (r+1,c) in arr:
            value -= 2
        if (r-1, c) in arr:
            value -= 2
        if (r, c+1) in arr:
            value -= 2
        if (r, c-1) in arr:
            value -= 2
    print(value)
