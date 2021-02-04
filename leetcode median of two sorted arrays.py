a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=len(a)
y=len(b)
if y > x:
    x, y = y, x
    a, b = b, a
start=0
end=n
while(start<=end):
    xpart=(start+end)//2
    ypart = ((x+y+1)//2)-xpart

    if xpart < x and b[ypart-1] > a[xpart]:
        start = xpart+1
    elif xpart > 0 and a[xpart-1] > b[ypart]:
        end = xpart-1
    else:
        if xpart==0:
            max_left = b[ypart-1]
        elif ypart==0:
            max_left = a[xpart-1]
        else:
            max_left = max(a[xpart-1], b[ypart-1])

        if (x+y)%2!=0:
            return max_left

        if xpart==x:
            min_right = b[ypart]
        elif ypart==y:
            min_right = a[xpart]
        else:
            min_right = min(a[xpart],b[ypart])

        return (max_left+min_right)/2
