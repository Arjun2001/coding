# def getpos(n):
#     index = -1
#     n = str(n)
#     for i in range(len(n)):
#         if int(n[i])%2 != 0:
#             index = i
#             break
#     return index

# n = 6013
# temp = getpos(n)
# if temp == -1:
#     print(0)
# else:
#     n = str(n)
#     sdf= ""
#     for i in range(temp,len(n)):
#         sdf += n[i]
#     n = sdf
#     print(n)
#     new_len = len(n)-1
#     start_index = int(n[0])
#     upper_bound = start_index + 1
#     upper_bound = "" + str(upper_bound) + '0'*new_len
#     lower_bound = '8'
#     lower_bound *= new_len
#     if start_index - 1 != 0:
#         lower_bound = str(start_index-1) + (lower_bound)
#     print(upper_bound,lower_bound)
#     print(min(int(upper_bound)-int(n), int(n)-int(lower_bound)))
# 2   1   1
# 0   1   0
# 0   1   1
# import sys
# n,m,t,c = 5,5,5,3
# sdf = [[1,2],[2,3],[3,4],[1,5]]
# edges = {}
# for i in sdf:
#     if i[0] not in edges:
#         edges[i[0]] = []
#     edges[i[0]].append(i[1])
#     if i[1] not in edges:
#         edges[i[1]] = []
#     edges[i[1]].append(i[0])

# visited = [0]*(n+1)
# q = [1]
# visited[1] = 1
# dist = [sys.maxsize]*(n+1)
# dist[1] = 0

# while (len(q)!=0):
#     l = len(q)
#     curr = q.pop(0)
#     for i in edges[curr]:
#         if visited[i] == 0:
#             visited[i] = 1
#             dist[i] = min(dist[i],dist[curr]+1)
#             print(curr," -> ", i,dist)
#             if i == n:
#                 q = []
#                 break
#             for j in edges[i]:
#                 q.append(j)
#                 if j == n or visited[j]==0:
#                     dist[j] = min(dist[j],dist[i]+1)
# print(dist[5])
def solve(a,b,n,m):
    if n == 0 or m == 0:
        return 0
    if a[n-1] == b[m-1]:
        return 1+ solve(a,b,n-1,m-1)
    else:
        return max(solve(a,b,n-1,m), solve(a,b,n,m-1))     

a = "agbcbga"
b = a[::-1]
print(solve(a,b,len(a),len(b)))