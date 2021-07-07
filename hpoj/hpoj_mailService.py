def func(i):
    ans = d[i] - total_dist[i+1] + dist2origin[i+1]
    return ans

def prnt(val):
    print(val)


def solve(c,n):
    i = 1
    while(i <= n):
        x[i],y[i],w = list(map(int,input().split()))
        dist2origin[i] = abs(x[i]) + abs(y[i])
        total_dist[i] = total_dist[i-1]+abs(x[i]-x[i-1]) + abs(y[i]-y[i-1])
        total_weight[i] = total_weight[i-1] + w
        i += 1
    front = rear = 1
    i = 1
    while(i <= n):
        while((front <= rear) and (total_weight[i] - total_weight[q[front]]) > c):
            front += 1
        d[i] = func(q[front]) + total_dist[i] + dist2origin[i]
        while(front <= rear and (func(i) <= func(q[rear]))):
            rear -= 1
        rear += 1
        q[rear] = i
        i += 1
    return(d[n])
    

tc = int(input())
while(tc):
    temp = input()
    c = int(input())
    n = int(input())
    maxn = n+10
    x = [0]*maxn
    y = [0]*maxn
    total_dist = [0]*maxn
    total_weight = [0]*maxn
    dist2origin = [0]*maxn
    q = [0]*maxn
    d = [0]*maxn
    total_dist[0] = total_weight[0] = x[0] = y[0] = 0
    answer = solve(c,n)
    prnt(answer)
    tc -= 1
    if (tc > 0):
        prnt('')
