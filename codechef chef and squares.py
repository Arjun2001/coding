for _ in range(int(input())):
    n = int(input())
    flag = 0
    for i in range(int(n**0.5),0,-1):
        if n%i == 0:
            x = ((n//i)+i)//2
            m = ((n//i)-i)//2
            if n+(m*m) == (x*x) and (n//i != i):
                print(m*m)
                flag = 1
                break
    if flag == 0:
        print('-1')
