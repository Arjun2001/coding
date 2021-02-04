test = int(input())
while(test):
    test -= 1
    a = input()
    b = input()
    count = 0
    i = 0
    while (i<len(a)):
        print(i,"i")
        if a[i]!=b[i]:
            while( i < len(a) and a[i]!= b[i]):
                i += 2
            count += 1
        i += 2
    i = 1
    while(i<len(a)):
        if a[i]!=b[i]:
            while( i < len(a) and a[i] != b[i]):
                i += 2
            count += 1
        i += 2
    print(count)
