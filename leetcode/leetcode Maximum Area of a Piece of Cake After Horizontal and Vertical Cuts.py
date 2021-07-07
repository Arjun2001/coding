h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
hor = horizontalCuts
hor.sort()
ver = verticalCuts
ver.sort()
hmax = max(hor[0],h-hor[-1])
vmax = max(ver[0],w-ver[-1])
for i in range(1,len(hor)):
    hmax = max(hmax,hor[i]-hor[i-1])
for i in range(1,len(ver)):
    vmax = max(vmax,ver[i]-ver[i-1])
print(hmax*vmax)
