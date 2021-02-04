import math
tc = int(input())
for i in range(tc):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    j = 0
    while (x > 0 and j < n-1):
        flag = 0
        p = int(math.log(a[j],2))
        temp = (1<<p)
        a[j] = a[j]^temp
        for k in range(j+1,n):
            if a[j]^temp < a[j]:
                a[j] = a[j]^temp
                flag = 1
                break
        if flag == 0:
            a[n-1] = a[n-1]^temp
        while( a[j] <= 0):
            j += 1
        x -= 1
    z = x+1
    if z > 0:
        if n < 3 and z%2 == 0:
            a[n-1] = a[n-1]^1
            a[n-2] = a[n-2]^1
    for i in a:
        print(i, end = ' ')
    print('')
                
