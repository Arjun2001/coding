import math
from sys import stdin
for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    count=0
    if n<=700:
        a=1
        while 1:
            x=n-(a**2)
            if x>0:
                count+=x
            else:
                break
            a+=1
    else:
        amin=int(math.sqrt(n-700))
        count=amin*700
        i=amin+1
        while 1:
            x=n-(i**2)
            if x>0:
                count+=x
            else:
                break
            i+=1
    print(count)
        
        