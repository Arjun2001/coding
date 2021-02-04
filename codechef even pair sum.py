tc = int(input())
for i in range(tc):
    t1 = t2 =0
    a,b = map(int,input().split())
    t1 = a//2
    t2 = b//2
    print((t1*t2)+((a-t1)*(b-t2)))
