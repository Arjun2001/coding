for _ in range(int(input())):
    D,d,p,q = list(map(int,input().split()))
    money = 0
    remaining = 0
    if d == 1:
        num = D
    else:
        num = D//d
        remaining = D%d
    money += D * p
    q_num = (num*(num-1))//2
    money += q_num*q*d
    if remaining:
        money += num * q *remaining
    print(money)
        