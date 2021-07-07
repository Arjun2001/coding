import math
for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans_map = {}
    for i in arr:
        while i != 0:
            nearest_pow = int(math.log2(i))
            remainder = i - int(math.pow(2,nearest_pow))
            if nearest_pow not in ans_map:
                ans_map[nearest_pow] = 0
            ans_map[nearest_pow] += 1
            i = remainder
    ans = 0
    for i in (ans_map):
        ans += math.ceil(ans_map[i]/k)
    print(ans)

