for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ite = (n//k)
    no = int(n%k)
    if no!=0: ite2 = ite+1
    cost = 0
    for i in range(n-1,n-k-1,-1):
        if no > 0:
            for j in range(ite2):
                cost += ((j+1)*a[i-(k*j)])
            no -= 1
        else:
            for j in range(ite):
                cost += ((j+1)*a[i-(k*j)])
    print(cost%1000000007)
        
