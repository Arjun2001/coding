import sys
import math

def findy(x1,y1,x2,y2,x):
    return ( (((y2-y1)/(x2-x1))*(x-x1))+y1 )

def dist(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def printFn(total):
    print(round(total,2))

def solve(n):
    graph = {}
    maxx = -sys.maxsize - 1
    minx = sys.maxsize
    miny = 0
    maxy = 0
    total = 0
    for i in range(n):
        x,y = map(int,input().split())
        graph[x] = y
        if(maxx <= x):
            maxx = x
            maxy = y
        if(minx >= x):
            minx = x
            miny = y
    temp = minx
    curpx = temp
    temp = miny
    curpy = temp
    for x in sorted(graph.keys()):
        if(x == minx):
            continue
        yline = findy(minx,miny,maxx,maxy,x)
        if(yline < graph[x]):
            total += dist(curpx,curpy,x,graph[x])
            curpx = x
            curpy = graph[x]
            del graph[x]

    for x in sorted(graph.keys(),reverse=True):
        total += dist(curpx,curpy,x,graph[x])
        curpx = x
        curpy = graph[x]
        del graph[x]    

    printFn(total)

for _ in range(int(input())):
    n = int(input())
    solve(n)