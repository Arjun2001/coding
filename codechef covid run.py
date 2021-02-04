test=int(input())
while(test):
    test-=1
    n,k,x,y=list(map(int,input().split()))
    temp=x
    temp1=1
    sol=0
    while(temp!=x or temp1==1):
        temp1=0
        if temp==y:
            print("YES")
            sol=1
            break
        temp=(temp+k)%n
    if sol==0:
        print("NO")
