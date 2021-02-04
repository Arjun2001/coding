for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    sumi = sum(a)
    if sumi%k == 0:
        print('0')
    else:
        print('1')
