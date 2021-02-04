test=int(input())
while(test):
    p,h=list(map(int,input().split()))
    while( p>0 and h>0):
        p=p-h
        h=int(h/2)
    if p<=0:
        print('1')
    else:
        print('0')
    test-=1
