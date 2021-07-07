n = 100001
prime = [0 for i in range(n+1)]
i = 2
while i<= n:
    if prime[i]==0:
        for j in range(i,n+1,i):
            prime[j] += 1
    i += 1

f = []
arr = [0]*6
for i in range(n):
    if prime[i] <=5 :
        arr[prime[i]] += 1
    f.append(arr[:])

for _ in range(int(input())):
    a,b,k = map(int,input().split())
    print(f[b][k]-f[a-1][k])
