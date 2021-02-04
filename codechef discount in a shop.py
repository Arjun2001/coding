for _ in range(int(input())):
    n = input()
    ans = int(n)
    temp = ''
    for i in range(len(n)):
        temp = n[:i] + n[i+1:]
        ans = min(ans , int(temp))
    print(ans)
