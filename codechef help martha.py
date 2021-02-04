test=int(input())
while(test):
    from sys import stdin, stdout
    thisdict = {"R": 0,"L": 0,"U": 0,"D": 0}
    a=input()
    for i in range(len(a)):
        thisdict[a[i]]+=1
    x,y=list(map(int,input().split()))
    n=int(input())
    while(n):
        x1,y1=map(int,stdin.readline().split())
        l=x1-x
        m=y1-y
        check=1
        if l>0:
            if thisdict['R']<l:
                check=0
        else:
            if thisdict['L']<abs(l):
                check=0
        if m>0:
            if thisdict['U']<m:
                check=0
        else:
            if thisdict['D']<abs(m):
                check=0
        if check==1:
            stdout.write("YES " + str(abs(l)+abs(m)) + '\n')
        else:
            stdout.write("NO" + '\n')
        n-=1
    test-=1
