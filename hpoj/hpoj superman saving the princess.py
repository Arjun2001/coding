import sys

def printfn(val):
    print(val)

def solve(t,max_int):
    while(t):
        g = [[max_int for x in range (15)]for i in range(15)]
        can = [[0 for x in range (15)]for i in range(15)]
        dis = [[max_int for x in range (15)]for i in range(15)]
        a,b,m,l,k = list(map(int,input().split()))
        tempa = 0
        tempa += a+b+1
        p = 1
        i = 1
        while(i<=m):
            x,y,z = list(map(int,input().split()))
            g[x][y]=g[y][x]=z
            if(z <= l):
                can[x][y]=can[y][x]=1
            i += 1
        
        for i in range(0,tempa-1):
            g[i+1][i+1]=0
        for x in range(1,tempa):
            for i in range(1,tempa+1):
                for j in range(1,tempa):
                    if(g[i][x]+g[x][j] < g[i][j]):
                        summa = g[x][j] +g[i][x]
                        g[i][j]= summa
                        if a>=x:
                            if l>=g[i][j]:
                                can[i][j]=can[j][i]=1

        for i in range(0,tempa-1):
            dis[i+1][0]=g[p][i+1]

        i = 0
        while (i <= k):
            dis[p][i]=0
            i+=1
        i = 2
        while(i<tempa):
            for h in range(1,k+1):
                minn=sys.maxsize
                for j in range(1,i):
                    if(can[i][j]):
                        if minn > dis[j][h-1]:
                            minn = dis[j][h-1]
                    if (minn > dis[j][h]+g[j][i]):
                        minn = dis[j][h]+g[j][i]
                dis[i][h]=minn
            i += 1
        printfn(dis[tempa-1][k])
        t -= 1

t=int(input())
max_int = sys.maxsize
solve(t,max_int)
