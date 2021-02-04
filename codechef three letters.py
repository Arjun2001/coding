for _ in range(int(input())):
    a = input()
    d = dict()
    for i in a:
        if i not in d:
            d[i] = 0
        d[i] += 1
    one = two = 0
    for i in d:
        two += d[i]//2
        one += d[i]%2
    if two <= one:
        print(two)
    else:
        print(one+(two-one)*2//3)
        
