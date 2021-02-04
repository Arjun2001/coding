for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    z = z1 = count = 0
    flag = 1
    for i in range(n):
        if a[i] == '0':
            z += 1
        if b[i] == '0':
            z1 += 1
        if a[i] != b[i]:
            if a[i] == '1':
                count += 1
            else:
                count -= 1
            if count < 0:
                flag = 0
                break
    if flag and z==z1:
        print('Yes')
    else:
        print('No')
