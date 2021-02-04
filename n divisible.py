def recur(n,arr):
    if sum(arr) == n:
        print(arr)
        return 0
    for i in range(1, n+1):
        if sum(arr)+i <= n:
            arr.append(i)
        else:
            return
        recur(n,arr)
        arr.pop()
    

n = int(input())
a = []
recur(n, a)
