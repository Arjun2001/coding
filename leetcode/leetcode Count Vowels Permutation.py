MOD = 10 ** 9 + 7
n = 2
a,e,i,o,u = [1]*n, [1]*n, [1]*n, [1]*n, [1]*n
for j in range(1,n):
    a[j] = (e[j-1] + u[j-1] + i[j-1]) % MOD
    e[j] = (a[j-1] + i[j-1]) % MOD
    i[j] = (e[j-1] + o[j-1]) % MOD
    o[j] = (i[j-1] ) % MOD
    u[j] = (o[j-1] + i[j-1]) % MOD
print(a,e,i,o,u)
print((a[n-1] + e[n-1] + i[n-1] + o[n-1] + u[n-1]) % MOD) 