for _ in range(int(input())):
    n = int(input())
    x = 1
    while x*2<=n:
        x*=2
    fib = []
    for i in range(60):
        if i==0:
            fib.append(0)
        elif i==1:
            fib.append(1)
        else:
            fib.append((fib[-1]+fib[-2])%10)
        
    print(fib[(x%60)-1])
