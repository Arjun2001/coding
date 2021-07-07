def printFn(total,possible,n):
    if (total == 0 and possible == n):
        print("Yes")
    else:
        print("No")

def solve(n,a,b):
    arr = list(map(int,input().split()))
    total = -1*a
    total = total*b
    less = min(a,b)
    large = max(a,b)
    possible = 0
    index = 0
    for i in range(0,n):
        total += arr[index]
        if (total <=0 and possible == i):
            j = 1
            while(j*j <= arr[index]):
                if (arr[index] % j == 0 and j<=less and arr[index]/j <= large):
                    possible += 1
                    break
                j += 1
        index += 1
    printFn(total,possible,n)



for _ in range(int(input())):
    n = int(input())
    a,b = list(map(int,input().split()))
    solve(n,a,b)
    
