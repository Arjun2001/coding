for k in range(int(input())):
    n,m,l = list(map(int,input().split()))
    d = {}
    for i in range(l):
        temp = input().split(":")
        name = temp[0]
        d[name] = 0
        temp = temp[1].split(',')
        te1 = n
        te2 = m
        while(te1 != te2):
            if (((te1//2) >= te2) and ((te1//2)*int(temp[0])) > int(temp[1])):
                te1 = te1//2
                d[name] += int(temp[1])
            elif(te1-1 >= te2):
                te1 -= 1
                d[name] += int(temp[0])
    print("Case",k+1)
    for i in sorted(d, key=d.get):
        print(i,d[i])