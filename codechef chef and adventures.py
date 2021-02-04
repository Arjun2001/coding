for _ in range(int(input())):
    n, m, x, y = map(int,input().split())
    if (((n-1)%x==0) and ((m-1)%y==0) and n>=1 and m>=1) or ((n-2)%x==0 and (m-2)%y==0 and n>=2 and m>=2) or (n==2 and m == 2):
        print('Chefirnemo')
    else:
        print('Pofik')
        
