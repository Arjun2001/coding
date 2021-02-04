t = int(input())
while(t):
    k,d0,d1=list(map(int,input().split()))
    s=d0+d1
    c=((2*s)%10)+((4*s)%10)+((8*s)%10)+((6*s)%10)
    if (k==2):
        tot = s
    else:
        no_cycles = (k-3)//4
        left_over = (k-3)-(no_cycles*4)
        tot = s+(s%10) + (no_cycles*c)
        p=2
        for i in range(left_over):
            tot+=(p*s)%10
            p=(p*2)%10       
    
    if(tot%3==0):
        print('YES')
    else:
        print("NO")
    t-=1
