import math
for _ in range(int(input())):
    n, a, b, k = map(int,input().split())
    count = n//a
    count += n//b
    count -= (2*(n//((a*b)//math.gcd(a,b))))
    if count >= k:
        print('Win')
    else:
        print('Lose')
