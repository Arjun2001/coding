from collections import defaultdict

class Graph:
    def __init__(self,num_of_edges):
        self.num_of_edges =  num_of_edges
        self.edges = defaultdict(list)

    def add_edge(self,u,v):
        self.edges[u].append(v)

class Dsu:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank
    
def union(subset,u,v):
    if subset[u].rank > subset[v].rank:
        subset[v].parent = u
        subset[u].rank += subset[v].rank
    elif subset[v].rank > subset[u].rank:
        subset[u].parent = v
        subset[v].rank += subset[u].rank
    else:
        subset[v].parent = u
        subset[u].rank += 1

def find(subnet,u):
    if subnet[u].parent != u:
        subnet[u].parent = find(subnet,subnet[u].parent)
    return subnet[u].parent

def isCycle(graph):
    subnet = []
    for i in range(graph.num_of_edges):
        subnet.append(Dsu(i,0))

    for u in graph.edges:
        u_rep = find(subnet,u)
        for v in graph.edges[u]:
            v_rep = find(subnet,v)
            if u_rep == v_rep:
                return True
            else:
                union(subnet,u_rep,v_rep)



g = Graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,2)

if isCycle(g):
	print('Graph contains cycle')
else:
	print('Graph does not contain cycle')

