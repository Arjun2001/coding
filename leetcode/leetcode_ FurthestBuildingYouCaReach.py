import heapq
heights = [14,3,1,3]
bricks = 17
ladders = 0
l = len(heights)
heap = []
heapq.heapify(heap)
ans = l-1
for i in range(l-1):
    temp = heights[i+1] - heights[i]
    if temp <=0:
        continue
    ladders -= 1
    heapq.heappush(heap,temp)
    if ladders < 0:
        temp = heapq.heappop(heap)
        if bricks < temp:
            ans = i
            break
        else:
            bricks -= temp
print(ans)



