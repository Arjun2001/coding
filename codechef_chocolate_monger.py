for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
    if (len(d)+x <= n):
        print(len(d))
    else:
        print(n-x)