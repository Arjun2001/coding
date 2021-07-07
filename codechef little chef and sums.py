for _ in range(int(input())):
    n =  int(input())
    a = list(map(int,input().split()))
    index = 0
    mini = a[0]
    for i in range(n):
        if mini > a[i]:
            mini = a[i]
            index = i
    print(index+1)