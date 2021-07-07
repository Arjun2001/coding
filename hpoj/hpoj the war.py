for k in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l = sorted(l,key=lambda x:x[1], reverse = True)
    temp = 0
    for i in range(0,n):
        temp += l[i][0]
    temp += l[n-1][1]
    temp1 = temp
    for i in range(n-1):
        temp1 -= l[i-1][0]
        if temp1 < l[i][1]:
            temp = l[i][1]

    print("Testcase"+str(k+1)+":"+str(temp))