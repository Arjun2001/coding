import math
for _ in range(int(input())):
    n = int(input())
    arr = [0]*(n+1)
    a = list(map(int,input().split()))
    for i in a:
        arr[int(math.sqrt(i))]=1
    for i in range(1,n+1):
        if arr[i]==0:
            print(i*i)
        
