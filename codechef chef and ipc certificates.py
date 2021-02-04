n, m , k = list(map(int,input().split()))
ans = 0
for i in range(n):
    temp = list(map(int,input().split()))
    if temp[k]<=10:
        count = 0
        for j in range(k):
            count += temp[j]
        if count>=m:
            ans += 1
print(ans)
