test=int(input())
while(test):
    test-=1
    n=int(input())
    temp=1
    query=0
    ans=[]
    for i in range(20):
        query=query|(temp<<i)
        print(1,query)
        ans.append(int(input()))

    sol=0
    if (n%2==0 and ans[0]%2==1) or (n%2==1 and ans[0]%2==0):
        sol=1
        
    for i in range(1,len(ans)):
        temp=abs(ans[i]-ans[i-1])
        temp=temp>>i
        if ans[i] < ans[i-1]:
            ones=((n+temp)//2)
        else:
            ones=((n-temp)//2)
        if ones%2==1:
            sol=sol|(1<<i)
    print(2,sol)
    fin_sol=int(input())
    if fin_sol==-1:
        break
