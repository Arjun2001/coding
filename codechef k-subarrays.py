from sys import maxsize
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = list(map(int,input().split()))
    maxi = -maxsize - 1
    temp = 0
    ans = []
    for i in arr:
        temp += i
        maxi = max(maxi,temp)
        if temp < 0:
            temp = 0
    print(maxi)