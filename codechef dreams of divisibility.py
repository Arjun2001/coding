import math

def lcmfunc(a, b) :
    return (a*b)//math.gcd(a, b)


for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    flag = 0
    for i in range(n):
        if a[i]%k != 0:
            lcm = lcmfunc(a[i],k)
            factor = lcm // a[i]
            factor1 = int(math.log(factor,2))
            if math.pow(2, factor1) != factor:
                print('NO')
                flag = 1
                break
    if flag == 0:
        print('YES')      