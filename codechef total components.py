# class Dsu:
#     def __init__(self,parent,rank):
#         self.parent = parent
#         self.rank = rank

# def union(subset,u,v):
#     if subset[u].rank > subset[v].rank:
#         subset[v].parent = u
#         subset[u].rank += subset[v].rank
#     elif subset[v].rank > subset[u].rank:
#         subset[u].parent = v
#         subset[v].rank += subset[u].rank
#     else:
#         subset[v].parent = u
#         subset[u].rank += 1

# def find(subnet,u):
#     if subnet[u].parent != u:
#         subnet[u].parent = find(subnet,subnet[u].parent)
#     return subnet[u].parent


 

# for _ in range(int(input())):
#     n = int(input())
#     subnet = []
#     subnet.append(0)
#     subnet.append(0)
#     ans = 0
#     for i in range(2,n+1):
#         subnet.append(Dsu(i,0))
#     for i in range(3,n+1):
#         if (i%2 == 0):
#             union(subnet,2,i)
#         else:
#             if (i*2 <= n+1):
#                 union(subnet,2,i)
#             else:
#                 ans += 1



    
n1 = 10000000+1
prime = [True for i in range(n1)]
p = 2
while(p * p <= n1):
    if (prime[p] == True):
        for i in range(p * p, n1, p):
            prime[i] = False
    p += 1

for i in range(int(input())):
    n = int(input())
    ans = 1
    for j in range(3,n+1):
        if j%2 != 0:
            if j*2 > n and prime[j]:
                ans += 1
    print(ans)
