cost = [10,15,20]
l = len(cost)
for i in range(l-1,-1,-1):
    if i + 1 < l and i + 2 < l:
        cost[i] += min(cost[i+1],cost[i+2])
print(min(cost[0],cost[1]))
