import sys 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
        self.ans = 0
 
    def printMST(self, parent):
        for i in range(1,self.V):
            self.ans = self.ans + self.graph[i][parent[i]]
        return self.ans
 
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
 
    def primMST(self):
        self.ans = 0
        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0   
        mstSet = [False] * self.V
        parent[0] = -1   
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return self.printMST(parent)            
 
input1 = list(map(int ,input().split(" ")))
n_nodes = input1[0]
n_query = input1[1]
g = Graph(n_nodes)
for i in range(n_nodes):
    list1 = list(map(int ,input().split(" ")))
    g.graph[list1[0]-1][list1[1]-1] = list1[2]
    g.graph[list1[1]-1][list1[0]-1] = list1[2]
for i in range(n_query):
    query = list(map(int ,input().split(" ")))
    a = query[0] + (g.ans % 100)
    b = query[1] + (g.ans % 100)
    u = query[2] + (g.ans % 100)
    v = query[3] + (g.ans % 100)
    c = query[4] + (g.ans % 100)
    g.graph[a-1][b-1] = 0
    g.graph[b-1][a-1] = 0
    g.graph[v-1][u-1] = c
    g.graph[u-1][v-1] = c
    print(g.primMST())