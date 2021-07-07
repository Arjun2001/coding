for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(k) :
        d = {}
        max_so_far =  1
        total = 0
        for j in range(i,n,k):
            total += 1
            if (arr[j] in d):
                d[arr[j]] += 1
                max_so_far = max(max_so_far,d[arr[j]])
            else:
                d[arr[j]] = 1
        ans += total - max_so_far
    print(ans)
            

