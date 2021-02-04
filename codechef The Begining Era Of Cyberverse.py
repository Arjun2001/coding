for _ in range(int(input())):
    n, k = map(int,input().split())
    if k >= n:
        ans = k//n
        print(ans)
    else:
        print('0')
