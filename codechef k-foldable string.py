test=int(input())
while(test):
    dict1={'0':0, '1':0}
    n,k=list(map(int,input().split()))
    a=input()
    for i in range(n):
        dict1[a[i]]+=1
    val=n//k
    zero=dict1['0']
    one=dict1['1']
    if (zero%val==0 and one%val==0):
        zeroc=zero//val
        onec=one//val
        temp='0'*zeroc
        temp+='1'*onec
        rev=temp[::-1]
        temp1=''
        for i in range(val):
            if i%2==0:
                temp1+=temp
            else:
                temp1+=rev
        print(temp1)
    else:
        print("IMPOSSIBLE")
    test-=1
    
