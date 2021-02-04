for _ in range(int(input())):
    n = int(input())
    len1 = len2 =0
    for j in range(n):
        a = list(map(int,input().split()))
        for i in range(1,a[0]+1):
            if a[i] > 0:
                len1 += 1
            else:
                len2 += 1
    print(len1*len2)
