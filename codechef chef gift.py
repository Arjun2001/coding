def gcd(a, b): 
    if (a == 0 or b == 0): return 0
    if (a == b): return a 
    if (a > b):  
        return gcd(a - b, b) 
    return gcd(a, b - a) 


test = int(input())
while(test):
    test -= 1
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        left = 1
        for j in range(0,i+1):
            left *= a[j]
        right = 1
        for k in range(i+1,n):
            right *= a[k]

        if gcd(left,right) == 1:
            print(i+1)
            break
        
