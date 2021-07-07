for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ctr = 0
    for i in range(n):
        if a[i]%2 == 0:
            ctr += 1
    print(min(ctr,n-ctr))