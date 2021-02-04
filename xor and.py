arr=list(map(int,input().split()))
newmax=0
mask=0
maxx=0
s=set()
for i in range(31, -1, -1):
    mask |=(1<<i)
    newmax = maxx | (1<<i)
    for i in range(len(arr)):
        s.add(arr[i]&mask)
    for prefix in s:
        print(prefix)
        if (prefix ^ newmax) in s:
            print(s,prefix,newmax,prefix ^ newmax)
            maxx = newmax
            break
    s.clear()
print(maxx)
