for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        temp = a[i] + a[(i+1)%n] + a[(i+2)%n]
        ans = max(ans, temp)
    print( ans )