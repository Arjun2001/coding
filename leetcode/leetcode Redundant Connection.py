def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    pa_x = find(x)
    pa_y = find(y)
    if pa_x == pa_y:
        return False
    else:
        parent[pa_x] = pa_y
    return True


edges = [[1,2],[1,3],[2,3]]
parent = [x for x in range(len(edges)+1)]
for x,y in edges:
    if not union(x,y):
        print ([x,y])
        break
    print(parent)
