import math

m , w, p, n = 1,1,6,45
candy = 0
ans = math.ceil(n/(m*w))
turns = 0
prod = 0
while (turns < ans):
    prod = m*w
    if p > candy:
        days = math.ceil((p-candy)/(m*w))
        candy += days*prod
        turns += days
    available = candy//p
    no_buy = min(abs(m-w),available)
    if m < w:
        m += no_buy
    else:
        w += no_buy
    rem = available - no_buy
    m += rem//2
    w += rem - (rem//2)
    candy -= (available * p) 
    candy += m*w
    turns += 1
    remaining = max(n - candy,0)
    ans = min(ans,turns + math.ceil(remaining/(m*w)))
    
print(ans)
