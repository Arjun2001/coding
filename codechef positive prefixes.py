tc = int(input())
for i in range(tc):
    n, k = map(int,input().split())
    a = [j for j in range(1,n+1)]
    count = n-k
    index = 2
    temp = 1
    while(count>0):
        if index >= n :
            if a[n-1] > 0:
                index = n-1
            elif a[n-2] > 0:
                index = n-2
            temp = 0
        if temp:
            a[index] *= -1
            count -= 1
            index += 2
        if temp == 0:
            a[index] *= -1
            count -= 1
            index -= 2
    for i in a:
        print(i, end =" ")
    print('')
        
