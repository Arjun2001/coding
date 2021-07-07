def getVal(a,b):
    return mat[a+b-2] + a
    
mat = [0 for x in range(100000)]
for i in range(1,100000):
    mat[i] = mat[i-1] + i
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int,input().split())
    val = getVal(x1,y1)
    while x1 < x2:
        x1 += 1
        val += getVal(x1,y1)
    while y1 < y2:
        y1 += 1
        val += getVal(x1,y1)
    print(val)