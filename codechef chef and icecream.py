test=int(input())
while(test):
    store=[0,0,0]
    n=int(input())
    a=list(map(int,input().split()))
    check=1
    for i in range(n):
        check=0
        if(a[0]!=5):
            check=1
            break
        if(a[i]==5):
            store[0]+=1
        elif(a[i]==10):
            if store[0]>=1:
                store[0]-=1
                store[1]+=1
            else:
                check=1
                break
        elif(a[i]==15):
            if store[0]>=2 or store[1]>=1:
                store[2]+=1
                if store[1]>=1:
                    store[1]-=1
                else:
                    store[0]-=2
            else:
                check=1
                break        
    if check==1:
        print("NO")
    else:
        print("YES")
    test-=1
    
