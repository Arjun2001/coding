roads = [[1, 2], [1, 5], [3, 2], [2,4],[5,6],[7,5]]
n = 7
d = {}
for i in range(n-1):
    a,b = roads[i][0],roads[i][1]
    if a not in d:
        d[a] = 0
    d[a] += 1
    if b not in d:
        d[b] = 0
    d[b] += 1
inter = 0
for i,j in d.items():
    if j != 1:
        inter += 1
print(inter*2)