visited = []
jumps = []
forbid = []
na  = 0

def getArrayV(li):
    return (li[0]*1000 + li[1]*100 + li[2]*10 + li[3])

def getadjacent(u):
    tempadj = []
    global na
    global forbid
    na = 0
    if ( forbid[ ((u[0]+1)%10)*1000 + u[1]*100 + u[2]*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ ((u[0]+1)%10), u[1], u[2], u[3] ] )
    if ( forbid[ u[0]*1000 + ((u[1]+1)%10)*100 + u[2]*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ u[0], ((u[1]+1)%10), u[2], u[3] ] )
    if ( forbid[ u[0]*1000 + u[1]*100 + ((u[2]+1)%10)*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ u[0], u[1], ((u[2]+1)%10), u[3] ] )
    if ( forbid[ u[0]*1000 + u[1]*100 + u[2]*10 + ((u[3]+1)%10) ] ) == False:
        na += 1
        tempadj.append( [ u[0], u[1], u[2], ((u[3]+1)%10) ] )
    # down
    if ( forbid[ ((u[0]+9)%10)*1000 + u[1]*100 + u[2]*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ ((u[0]+9)%10), u[1], u[2], u[3] ] )
    if ( forbid[ u[0]*1000 + ((u[1]+9)%10)*100 + u[2]*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ u[0], ((u[1]+9)%10), u[2], u[3] ] )
    if ( forbid[ u[0]*1000 + u[1]*100 + ((u[2]+9)%10)*10 + u[3] ] ) == False:
        na += 1
        tempadj.append( [ u[0], u[1], ((u[2]+9)%10), u[3] ] )
    if ( forbid[ u[0]*1000 + u[1]*100 + u[2]*10 + ((u[3]+9)%10) ] ) == False:
        na += 1
        tempadj.append( [ u[0], u[1], u[2], ((u[3]+9)%10) ] )

    return tempadj

    


def bfs(start, end):
    global na
    global visited
    global jumps
    global forbid
    q = []
    q.append(start)
    visited[getArrayV(start)] = True
    if (forbid[ start[0]*1000 + start[1]*100 + start[2]*10 + start[3] ] ):
        return -1
    while(len(q) != 0):
        temp = q.pop(0)
        if (temp == end):
            return jumps[getArrayV(temp)]
        adj = getadjacent(temp)
        for i in range(na):
            if (visited[getArrayV(adj[i])]):
                continue
            else:
                q.append(adj[i])
                visited[getArrayV(adj[i])] = True
                jumps[getArrayV(adj[i])] = jumps[getArrayV(temp)] + 1
    return -1


tc = int(input())
for i in range(tc):
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    visited = []
    jumps = []
    forbid = []
    for j in range(10000):
        visited.append(False)
        jumps.append(0)
        forbid.append(False)
    n = int(input())
    for j in range(n):
        forb = list(map(int,input().split()))
        forbid[forb[0]*1000 + forb[1]*100 + forb[2]*10 + forb[3]] = True
    print(bfs(start,end))
    if tc > 1 and i != (tc-1):
        temp = input()

