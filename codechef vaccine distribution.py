import math
tc = int(input())
for i in range(tc):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    if d == 1:
        print(math.ceil(n/d))
    else:
        risk = 0
        for j in range(n):
            if a[j] >= 80 or a[j] <= 9:
                risk += 1
        print(math.ceil(risk/d) + math.ceil((n-risk)/d))
