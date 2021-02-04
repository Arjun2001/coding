test=int(input())
while(test):
    n=int(input())
    for i in range(n):
        a,b=list(map(int,input().split()))
    if n<=5:
        print(n)
    else:
        temp=n
        while(n>5):
            n=(n//2)
            temp+=n
        print(temp)
    test-=1
