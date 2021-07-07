import bisect
n,q = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
count = 0
que = []
for i in range(q):
    ele = int(input())
    temp = bisect.bisect_left(arr,ele)
    if temp < len(arr) and arr[temp] == ele:
        print(0)
    else:
        if (temp%2 == 0):
            print("POSITIVE")
        else:
            print("NEGATIVE")
    