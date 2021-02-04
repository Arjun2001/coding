for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    temp = 0
    maxi = -1
    for i in range(n-1):
        for j in range(i+1,n):
            temp = abs(a[i]-a[j]) + abs(i-j)
            maxi = max(temp,maxi)
    print(maxi)
