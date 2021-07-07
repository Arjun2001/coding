import math
s = 'chillout'
s = "".join(s.split())
l = len(s)
sqrt = math.sqrt(l)
row = math.floor(sqrt)
column = math.ceil(sqrt)
for i in range(column):
    for j in range(0,l,column):
        if i+j < l:
            print(s[i+j], end = "")
    print(" ",end= "")
print()