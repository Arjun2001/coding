test = int(input())
while(test):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    left = right = 0
    for i in range(len(a)):
        if left > right :
            right += a[i]
        else:
            left += a[i]
    print(max(left,right))
    test -= 1
