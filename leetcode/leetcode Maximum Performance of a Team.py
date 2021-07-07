import heapq
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3

arr = sorted(zip(efficiency,speed),reverse=True)
tot_spd ,heap,ans = 0,[],0
for efe,spd in arr:
    heapq.heappush(heap,spd)
    if len(heap) <= k:
        tot_spd += spd
    else:
        tot_spd += spd - heapq.heappop(heap)
    ans = max(ans,tot_spd*efe)
print(ans)
