test = int(input())
while(test):
    test -= 1
    n, q = list(map(int,input().split()))
    ans = [0]*(n+1)
    a = list(map(int,input().split()))
    for i in range(q):
        maxi = count = 0
        x, y = list(map(int,input().split()))
        a[x-1] = y
        for i in range(n-1):
            if a[i] != a[i+1]:
                ans[i] = 1
                count += 1
            else:
                count = 0
            if i == n-2:
                if a[i] != a[i+1]:
                    a[n-1] = 1
                    count += 1
            maxi = max(maxi, count)
        print(maxi)
    
