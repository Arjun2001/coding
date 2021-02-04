for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    asum = sum(a)
    bsum = sum(b)
    if asum > bsum :
        print('0')
    else:
        a.sort()
        b.sort()
        ctr = 0
        flag = 0
        for i in range(n):
            if asum > bsum :
                print(ctr)
                flag = 1
                break
            temp1 = a[i]
            temp2 = b.pop()
            asum += temp2-temp1
            bsum += temp1-temp2
            ctr += 1
        if asum > bsum and flag == 0:
            print(ctr)
        elif flag != 1:
            print('-1')
