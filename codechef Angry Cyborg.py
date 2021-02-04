for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = [0]*n
    for p in range(k):
        l,r = map(int,input().split())
        temp = 1
        for i in range(l-1,r):
            arr[i] += temp
            temp += 1
    print(*arr)
        
