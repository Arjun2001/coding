d1, v1, d2, v2, p = list(map(int,input().split()))
vac = 0
days = min(d1,d2)-1
while (vac < p ):
    if d1 < d2 :
        d1 += 1
        days += 1
        vac += v1
    elif (d2 < d1):
        d2 += 1
        days += 1
        vac += v2
    else:
        d2 += 1
        d1 += 1
        days += 1
        vac += v1+v2
print(days)
