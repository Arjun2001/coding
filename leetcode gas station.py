gas=list(map(int,input().split()))
cost = list(map(int,input().split()))

fuel=0
n=len(gas)
ans=-1

for i in range(n):
    if gas[i]>cost[i]:
        fuel=gas[i]
        for j in range(i,(n+i)):
            if fuel>cost[i]:
                fuel=fuel+gas[(i+1)%n]-cost[i%n]
            else:
                ans=-1
            if fuel<0:
                ans=-1
        if j==(n+i-1) and ans!=-1:
            ans=i
            break

print(ans)
