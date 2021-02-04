for _ in range(int(input())):
    k, q = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    arr = []
    a.sort()
    b.sort()
    if k < 100:
        for i in a:
            for j in b:
                arr.append(i+j)
    else:
        maxi = a[101] + b[101]
        for i in a:
            for j in b:
                if maxi < i+j:
                    break
                arr.append(i+j)
    arr.sort()
    for _ in range(q):
        print(arr[int(input())-1])
                
