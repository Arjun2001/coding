for _ in range(int(input())):
    a,b,c,d,k = map(int,input().split())
    ans = abs(a-c)+abs(b-d)
    if ans == k:
        print("YES")
    elif k > ans and(k-ans) % 2 == 0:
        print("YES")
    else: 
        print("NO")