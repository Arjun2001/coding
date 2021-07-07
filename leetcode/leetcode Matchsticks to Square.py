def solve(i,n,match,sums):
    global visited
    print(i,n,visited,match,sums)
    if i >= len(match):
        return False
    if visited[i] == True:
        return False
    if sums == n:
        return True
    if sums > n:
        return False
    for temp in range(i,len(match)):
        print(temp)
        if visited[temp] == True:
            print("yeh")
            continue
        visited[temp] = True
        if not solve(temp+1,n,match,sums+match[temp]):
            visited[temp] = False
        else:
            print(temp,"here",visited)
            sums = 0
        
    return visited

match = [3,3,3,3,4]
l = len(match)
visited = [0]*l
s = sum(match)
if s % 4 != 0:
    print(False)
else:
    n = s // 4
    print("n =",n)
    print(solve(0,n,match,0))
