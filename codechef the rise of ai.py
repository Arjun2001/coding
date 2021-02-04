for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        a,b,c = map(int,input().split())
        temp1 = c//a
        temp2 = c//b
        print("dgfdf",temp1,temp2)
        if (c-(temp1*a))%b== 0 or (c-(temp2*b))%a == 0:
            ans += 1
    print(ans)
