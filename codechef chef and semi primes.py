def prime(n):
    p_no = []
    prim = [1]*(n+1)
    i = 2
    while (i*i<=n):
        if prim[i] == 1:
            for j in range(i*i,n+1,i):
                prim[j] = 0
        i += 1
    for i in range(2,n+1):
        if prim[i] == 1:
            p_no.append(i)
    return p_no

def subprime(arr):
    sub = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            sub.append(arr[i]*arr[j])
    return sub

ar = subprime(prime(200))
for _ in range(int(input())):
    n = int(input())
    ar.sort()
    flag = 1
    for i in ar:
        temp = n - i
        if i <= n:
            if temp in ar:
                print('YES')
                flag = 0
                break
            else:
                flag = 1
        else:
            flag = 1
            break
    if flag == 1:
        print('NO')















        
