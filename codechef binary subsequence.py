for _ in range(int(input())):
    n = int(input())
    a = input()
    zeros = ones = 0
    for i in range(n):
        if a[i] == '0':
            zeros += 1
        else:
            ones += 1
    ans = min (zeros, ones)
    one = 0
    zero = zeros
    for i in range(n):
        if a[i] == '1':
            one += 1
        else:
            zero -= 1
        ans = min(ans, one+zero)
    print(ans)

