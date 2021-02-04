test=int(input())
while(test):
    a=list(input())
    n=len(a)
    ans=0
    for i in range(len(a)):
        if a[i]=='x':
            if i+1<n and a[i+1]=="y":
                ans+=1
                a[i]="0"
                a[i+1]="0"
        if a[i]=='y':
            if i+1<n and a[i+1]=="x":
                ans+=1
                a[i]="0"
                a[i+1]="0"
    print(ans)
    test-=1
