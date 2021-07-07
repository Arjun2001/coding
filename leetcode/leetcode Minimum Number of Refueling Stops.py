from heapq import heappush,heappop,heapify
target = 100
startFuel = 1
stations = [[10,100]]
n = len(stations)
ans = 0
h = []
for i in range(n+1):
    dist = target if i == n else stations[i][0]
    if startFuel < dist:
        if len(h) == 0:
            print(-1)
            break
        startFuel -= heappop(h)
        ans += 1
    if i < n:
        heappush(h,-stations[i][1])
print(ans)